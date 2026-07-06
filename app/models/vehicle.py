from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String, nullable=False)
    driver_name = Column(String, nullable=False)
    current_location = Column(String)
    destination = Column(String)
    status = Column(String)