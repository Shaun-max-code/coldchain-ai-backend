from datetime import datetime

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey

from app.db.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    temperature = Column(Float)

    humidity = Column(Integer)

    speed = Column(Integer)

    latitude = Column(Float)

    longitude = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)