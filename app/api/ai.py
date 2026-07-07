from fastapi import APIRouter, HTTPException

from app.schemas.ai import AIRequest
from app.services.ai_service import analyze_vehicle
from app.services.simulator import simulate

router = APIRouter(
    prefix="/api/ai",
    tags=["AI"],
)


@router.post("/analyze")
def analyze(request: AIRequest):

    vehicles = simulate()

    vehicle = next(
        (v for v in vehicles if v["id"] == request.vehicle_id),
        None,
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found",
        )

    return analyze_vehicle(vehicle)