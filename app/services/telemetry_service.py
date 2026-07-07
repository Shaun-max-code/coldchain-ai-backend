from app.db.database import SessionLocal
from app.models.telemetry import Telemetry
from app.models.vehicle import Vehicle


def save_telemetry(truck):

    db = SessionLocal()

    # ---------------------------------------
    # Check if vehicle already exists
    # ---------------------------------------

    vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.id == truck["id"])
        .first()
    )

    # ---------------------------------------
    # First time seeing this truck
    # ---------------------------------------

    if vehicle is None:

        vehicle = Vehicle(
            id=truck["id"],
            vehicle_name=truck["vehicle"],
            driver_name=truck["driver"],
            current_location=f'{truck["lat"]}, {truck["lon"]}',
            destination="Medical Center",
            status=truck["status"],
        )

        db.add(vehicle)

    # ---------------------------------------
    # Existing truck
    # ---------------------------------------

    else:

        vehicle.current_location = f'{truck["lat"]}, {truck["lon"]}'
        vehicle.status = truck["status"]

    # ---------------------------------------
    # Save telemetry
    # ---------------------------------------

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