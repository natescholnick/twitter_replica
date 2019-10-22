from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)

# all variables based on this application must be instantiated after the app instance is created

bootstrap = Bootstrap(app)

# flask app instance uses from object method to laod in all configurartion variables
app.config.from_object(Config)

from app import routes
