import random

from app.services.telemetry_service import save_telemetry
from app.services.alert_service import check_alert

vehicles = [
    {
        "id": 1,
        "vehicle": "Truck-101",
        "driver": "John",
        "temperature": 4.2,
        "humidity": 60,
        "speed": 58,
        "lat": 10.031,
        "lon": 76.312,
    },
    {
        "id": 2,
        "vehicle": "Truck-102",
        "driver": "David",
        "temperature": 5.1,
        "humidity": 62,
        "speed": 61,
        "lat": 10.052,
        "lon": 76.338,
    },
]


def simulate():
    print("Simulator running...")

    for truck in vehicles:

        truck["temperature"] += random.uniform(-0.3, 0.5)
        truck["humidity"] += random.randint(-2, 2)
        truck["speed"] += random.randint(-3, 3)
        truck["lat"] += random.uniform(-0.001, 0.001)
        truck["lon"] += random.uniform(-0.001, 0.001)

        save_telemetry(truck)

        check_alert(truck)

    return vehicles