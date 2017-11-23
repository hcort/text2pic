from flask import Flask

# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

from app import views
