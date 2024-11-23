from dashboard import app
from dashboard.models import *

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    event = Event()
    event.save()


    return render_template('index.html', title='Home', events=Event.objects)