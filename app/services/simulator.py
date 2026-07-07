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

        # ====================================================
        # Vehicle Movement
        # ====================================================

        truck["lat"] += random.uniform(-0.0008, 0.0008)
        truck["lon"] += random.uniform(-0.0008, 0.0008)

        # Keep trucks around Kochi
        truck["lat"] = max(9.98, min(10.09, truck["lat"]))
        truck["lon"] = max(76.23, min(76.39, truck["lon"]))

        # ====================================================
        # Speed
        # ====================================================

        truck["speed"] += random.randint(-2, 2)
        truck["speed"] = max(35, min(80, truck["speed"]))

        # ====================================================
        # Humidity
        # ====================================================

        truck["humidity"] += random.randint(-1, 1)
        truck["humidity"] = max(50, min(75, truck["humidity"]))

        # ====================================================
        # Refrigeration Failure Simulation
        # ====================================================

        if not truck["fault"]:

            # ~2% chance refrigeration fails
            if random.random() < 0.02:
                truck["fault"] = True

        else:

            # ~5% chance technician fixes it
            if random.random() < 0.05:
                truck["fault"] = False

        # ====================================================
        # Temperature Behaviour
        # ====================================================

        if truck["fault"]:

            # Temperature rises continuously
            truck["temperature"] += random.uniform(0.25, 0.60)

        else:

            # Cooling system pulls temperature back toward 5°C
            target = 5.0

            truck["temperature"] += (
                (target - truck["temperature"]) * 0.15
            )

            truck["temperature"] += random.uniform(-0.08, 0.08)

        truck["temperature"] = round(
            max(2.0, min(15.0, truck["temperature"])),
            2,
        )

        # ====================================================
        # Fleet Status
        # ====================================================

        if truck["temperature"] >= 8:
            truck["status"] = "CRITICAL"

        elif truck["temperature"] >= 6:
            truck["status"] = "WARNING"

        else:
            truck["status"] = "SAFE"

        # ====================================================
        # Save Telemetry
        # ====================================================

        save_telemetry(truck)

        # ====================================================
        # Generate Alerts
        # ====================================================

        check_alert(truck)

    return vehicles