from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from mailer import mail

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mail.mail, 'interval', seconds=10)
    scheduler.start()