from app.db.database import SessionLocal
from app.models.telemetry import Telemetry


def save_telemetry(truck):

    db = SessionLocal()

    telemetry = Telemetry(
        vehicle_id=truck["id"],
        temperature=truck["temperature"],
        humidity=truck["humidity"],
        speed=truck["speed"],
        latitude=truck["lat"],
        longitude=truck["lon"],
    )

    db.add(telemetry)
    db.commit()
    db.close()