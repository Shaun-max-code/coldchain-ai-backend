from fastapi import APIRouter
from app.services.simulator import simulate

router = APIRouter(
    prefix="/api/vehicles",
    tags=["Vehicles"]
)

@router.get("/")
def get_vehicles():
    vehicles = simulate()

    return [
        {
            "id": v["id"],
            "vehicle": v["vehicle"],
            "driver": v["driver"],
            "temperature": v["temperature"],
            "humidity": v["humidity"],
            "speed": v["speed"],
            "latitude": v["lat"],      # <-- FIX
            "longitude": v["lon"], 
             "status": v["status"],      # <-- FIX
             "cargo": v["cargo"],
        }
        for v in vehicles
    ]