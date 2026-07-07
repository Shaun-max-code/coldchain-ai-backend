from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.telemetry import Telemetry

router = APIRouter(
    prefix="/api/telemetry",
    tags=["Telemetry"],
)


@router.get("/")
def get_telemetry():

    db: Session = SessionLocal()

    telemetry = (
        db.query(Telemetry)
        .order_by(Telemetry.timestamp.desc())
        .limit(100)
        .all()
    )

    db.close()

    return telemetry