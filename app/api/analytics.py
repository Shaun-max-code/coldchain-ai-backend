from fastapi import APIRouter

from app.services.analytics_service import get_dashboard_stats

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"],
)


@router.get("/")
def analytics():

    return get_dashboard_stats()