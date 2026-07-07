from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.alert import Alert

router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"],
)


@router.get("/")
def get_alerts():

    db: Session = SessionLocal()

    alerts = (
        db.query(Alert)
        .order_by(Alert.timestamp.desc())
        .limit(100)
        .all()
    )

    db.close()

    return alerts