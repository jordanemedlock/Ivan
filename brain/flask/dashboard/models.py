from dashboard import app

from flask_mongoengine import MongoEngine
from mongoengine import Document, DateTimeField


app.config['MONGODB_SETTINGS'] = {
    'db': 'dashboard',
    'host': 'mongo',
    'port': 27017
}
db = MongoEngine(app)

class Event(Document):
    event_time = DateTimeField()