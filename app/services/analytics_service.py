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

    # ----------------------------------------
    # Fleet Health
    # ----------------------------------------

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

    db.close()

    return {

        "fleetHealth": fleet_health,

        "activeVehicles": active_vehicles,

        "telemetryRecords": telemetry_records,

        "criticalAlerts": critical_alerts,

        "warningAlerts": warning_alerts,

        "averageTemperature": round(avg_temp or 0, 2),

        "highestTemperature": round(max_temp or 0, 2),
    }