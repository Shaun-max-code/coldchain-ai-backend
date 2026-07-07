import random

from app.services.telemetry_service import save_telemetry
from app.services.alert_service import check_alert

vehicles = [
    {
        "id": 1,
        "vehicle": "Truck-101",
        "driver": "John",
        "cargo": "Vaccines",
        "temperature": 4.5,
        "humidity": 60,
        "speed": 58,
        "lat": 10.031,
        "lon": 76.312,
        "status": "SAFE",
        "fault": False,
    },
    {
        "id": 2,
        "vehicle": "Truck-102",
        "driver": "David",
        "cargo": "Blood Plasma",
        "temperature": 5.2,
        "humidity": 62,
        "speed": 61,
        "lat": 10.052,
        "lon": 76.338,
        "status": "SAFE",
        "fault": False,
    },
    {
        "id": 3,
        "vehicle": "Truck-103",
        "driver": "Joseph",
        "cargo": "Frozen Fish",
        "temperature": 3.8,
        "humidity": 64,
        "speed": 55,
        "lat": 10.041,
        "lon": 76.285,
        "status": "SAFE",
        "fault": False,
    },
    {
        "id": 4,
        "vehicle": "Truck-104",
        "driver": "Thomas",
        "cargo": "Ice Cream",
        "temperature": 5.8,
        "humidity": 59,
        "speed": 60,
        "lat": 10.068,
        "lon": 76.301,
        "status": "SAFE",
        "fault": False,
    },
    {
        "id": 5,
        "vehicle": "Truck-105",
        "driver": "Rahul",
        "cargo": "Medicines",
        "temperature": 4.9,
        "humidity": 61,
        "speed": 57,
        "lat": 10.019,
        "lon": 76.327,
        "status": "SAFE",
        "fault": False,
    },
]


def simulate():

    print("Simulator running...")

    for truck in vehicles:

        # --------------------------
        # Vehicle movement
        # --------------------------

        truck["lat"] += random.uniform(-0.0008, 0.0008)
        truck["lon"] += random.uniform(-0.0008, 0.0008)

        truck["speed"] += random.randint(-2, 2)
        truck["speed"] = max(30, min(80, truck["speed"]))

        truck["humidity"] += random.randint(-1, 1)
        truck["humidity"] = max(50, min(75, truck["humidity"]))

        # --------------------------
        # Random refrigeration failure
        # --------------------------

        if not truck["fault"]:

            # Around 2% chance of failure each cycle
            if random.random() < 0.02:
                truck["fault"] = True

        # --------------------------
        # Temperature behaviour
        # --------------------------

        if truck["fault"]:

            # Temperature rises while refrigeration is faulty
            truck["temperature"] += random.uniform(0.25, 0.6)

            # Around 5% chance the fault gets fixed
            if random.random() < 0.05:
                truck["fault"] = False

        else:

            # Cooling system tries to maintain ~5°C
            ideal = 5.0

            truck["temperature"] += (
                (ideal - truck["temperature"]) * 0.15
            )

            truck["temperature"] += random.uniform(-0.08, 0.08)

        # Safety limits
        truck["temperature"] = round(
            max(2, min(15, truck["temperature"])),
            2
        )

        # Save telemetry
        save_telemetry(truck)

        # Alert service decides status
        check_alert(truck)

    return vehicles