from sqlalchemy import func

from app.db.database import SessionLocal
from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry


def get_dashboard_stats():

    db = SessionLocal()

    try:

        active_vehicles = db.query(Vehicle).count()

        telemetry_records = db.query(Telemetry).count()

        # Count alerts directly from vehicle status
        critical_alerts = (
            db.query(Vehicle)
            .filter(Vehicle.status == "CRITICAL")
            .count()
        )

        warning_alerts = (
            db.query(Vehicle)
            .filter(Vehicle.status == "WARNING")
            .count()
        )

        avg_temp = (
            db.query(func.avg(Telemetry.temperature))
            .scalar()
        )

        max_temp = (
            db.query(func.max(Telemetry.temperature))
            .scalar()
        )

        # Latest telemetry for fleet health
        latest = (
            db.query(Telemetry)
            .order_by(Telemetry.id.desc())
            .limit(active_vehicles)
            .all()
        )

        score = 0

        for t in latest:

            if t.temperature < 6:
                score += 100

            elif t.temperature < 8:
                score += 60

            else:
                score += 0

        fleet_health = 0

        if active_vehicles > 0:
            fleet_health = round(score / active_vehicles)

        return {

            "fleetHealth": fleet_health,

            "activeVehicles": active_vehicles,

            "telemetryRecords": telemetry_records,

            "criticalAlerts": critical_alerts,

            "warningAlerts": warning_alerts,

            "averageTemperature": round(avg_temp or 0, 2),

            "highestTemperature": round(max_temp or 0, 2),
        }

    finally:
        db.close()