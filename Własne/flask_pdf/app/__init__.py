from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from celery import Celery

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
celery = Celery(app.name,broker=app.config["CELERY_BROKER_URL"],backend=app.config["CELERY_RESULT_BACKEND"])
celery.conf.update(app.config)

from app import routes,database,actions



