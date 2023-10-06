#!flask/bin/python
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask

from text2pic.scheduler_task import scheduled_task
from text2pic.views import site

# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

site.static_folder = app.static_folder
app.register_blueprint(site)

sched = BackgroundScheduler(daemon=True)
sched.add_job(scheduled_task, 'interval', [app.static_folder], minutes=5)
sched.start()


@app.route('/')
def hello_guys():
    return '<h1>Hello from Flask-Docker!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
