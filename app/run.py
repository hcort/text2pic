#!flask/bin/python
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduler_task import scheduled_task


sched = BackgroundScheduler(daemon=True)
sched.add_job(scheduled_task,'interval',minutes=1)
sched.start()

#app = Flask(__name__)

if __name__ == "__main__":
    app.run()

#app.run(debug=True)
