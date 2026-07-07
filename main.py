from contextlib import asynccontextmanager
from app.api.health import router as health_router
from fastapi import FastAPI
from app.api.ai import router as ai_router

from app.db.database import Base, engine

# Import models (needed for SQLAlchemy to create tables)
from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry
from app.models.alert import Alert

# Import routers
from app.api.vehicles import router as vehicle_router
from app.api.telemetry import router as telemetry_router
from app.api.alerts import router as alert_router
from app.api.analytics import router as analytics_router

# Background scheduler
from app.services.scheduler import start_scheduler

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the simulator scheduler
    start_scheduler()
    yield


app = FastAPI(
    title="Cold Chain Dashboard API",
    version="1.0.0",
    lifespan=lifespan,
)

# Register all API routes
app.include_router(vehicle_router)
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