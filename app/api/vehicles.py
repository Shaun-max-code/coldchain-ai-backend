from fastapi import APIRouter

from app.services.simulator import simulate

router = APIRouter(
    prefix="/api/vehicles",
    tags=["Vehicles"]
)


@router.get("/")
def get_vehicles():

    return simulate()