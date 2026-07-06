from apscheduler.schedulers.background import BackgroundScheduler
from app.services.simulator import simulate

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(simulate, "interval", seconds=2)
    scheduler.start()