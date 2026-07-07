from app.db.database import SessionLocal
from app.models.alert import Alert


def check_alert(truck):

    db = SessionLocal()

    temp = truck["temperature"]

    if temp < 6:
        current_status = "SAFE"
    elif temp < 8:
        current_status = "WARNING"
    else:
        current_status = "CRITICAL"

    previous_status = truck.get("status", "SAFE")

    # Nothing changed
    if current_status == previous_status:
        db.close()
        return

    truck["status"] = current_status

    if current_status == "SAFE":

        alert = Alert(
            vehicle_id=truck["id"],
            alert_type="Temperature",
            severity="Recovered",
            temperature=temp,
            message=f'{truck["vehicle"]} temperature returned to normal.'
        )

    elif current_status == "WARNING":

        alert = Alert(
            vehicle_id=truck["id"],
            alert_type="Temperature",
            severity="Warning",
            temperature=temp,
            message=f'{truck["vehicle"]} temperature is approaching the upper limit.'
        )

    else:

        alert = Alert(
            vehicle_id=truck["id"],
            alert_type="Temperature",
            severity="Critical",
            temperature=temp,
            message=f'{truck["vehicle"]} exceeded the safe temperature limit!'
        )

    db.add(alert)
    db.commit()
    db.close()