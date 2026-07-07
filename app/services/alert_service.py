from app.db.database import SessionLocal
from app.models.alert import Alert


def check_alert(truck):

    db = SessionLocal()

    if truck["temperature"] >= 8:

        alert = Alert(
            vehicle_id=truck["id"],
            alert_type="Temperature",
            severity="Critical",
            temperature=truck["temperature"],
            message=f'{truck["vehicle"]} exceeded safe temperature!'
        )

        db.add(alert)

    elif truck["temperature"] >= 6:

        alert = Alert(
            vehicle_id=truck["id"],
            alert_type="Temperature",
            severity="Warning",
            temperature=truck["temperature"],
            message=f'{truck["vehicle"]} temperature rising.'
        )

        db.add(alert)

    db.commit()
    db.close()