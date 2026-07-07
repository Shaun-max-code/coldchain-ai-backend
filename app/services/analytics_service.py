from sqlalchemy import func

from app.db.database import SessionLocal
from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry
from app.models.alert import Alert


def get_dashboard_stats():

    db = SessionLocal()

    active_vehicles = db.query(Vehicle).count()

    telemetry_records = db.query(Telemetry).count()

    critical_alerts = (
        db.query(Alert)
        .filter(Alert.severity == "Critical")
        .count()
    )

    warning_alerts = (
        db.query(Alert)
        .filter(Alert.severity == "Warning")
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

    db.close()

    return {
        "activeVehicles": active_vehicles,
        "telemetryRecords": telemetry_records,
        "criticalAlerts": critical_alerts,
        "warningAlerts": warning_alerts,
        "averageTemperature": round(avg_temp or 0, 2),
        "highestTemperature": round(max_temp or 0, 2),
    }