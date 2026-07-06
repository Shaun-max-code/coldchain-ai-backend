from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.vehicle import Vehicle
from app.api.vehicles import router as vehicle_router
from app.services.scheduler import start_scheduler

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield


app = FastAPI(
    title="Cold Chain Dashboard API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(vehicle_router)


@app.get("/")
def root():
    return {
        "message": "Cold Chain Dashboard API Running 🚀"
    }