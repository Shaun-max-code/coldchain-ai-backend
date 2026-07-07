from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from app.db.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    alert_type = Column(String)
    severity = Column(String)
    message = Column(String)

    temperature = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)