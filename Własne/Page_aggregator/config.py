import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'haslo'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LENGTH = 10
    START_INDEX_INTERIA = 5
    START_INDEX_GAZETA = 1
    CELERY_BROKER_URL = "amqp://localhost//"
    CELERY_RESULT_BACKEND =  "amqp://localhost//"