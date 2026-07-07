from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine

# Routers
from app.api.health import router as health_router
from app.api.ai import router as ai_router
from app.api.vehicles import router as vehicles_router
from app.api.telemetry import router as telemetry_router
from app.api.alerts import router as alert_router
from app.api.analytics import router as analytics_router

# Models
from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry
from app.models.alert import Alert

# Scheduler
from app.services.scheduler import start_scheduler

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield


app = FastAPI(
    title="Cold Chain Dashboard API",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://cryoguard-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(vehicles_router)
app.include_router(telemetry_router)
app.include_router(alert_router)
app.include_router(analytics_router)
app.include_router(health_router)
app.include_router(ai_router)


@app.get("/")
def root():
    return {
        "message": "Cold Chain Dashboard API Running 🚚"
    }