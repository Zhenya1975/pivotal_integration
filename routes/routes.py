from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
# from models.models import SportDB, LeagueDB, TeamsDB, Match_statusDB, MatchesDB
from sqlalchemy import desc, asc
import pandas as pd
from datetime import datetime
import requests
import json


from extensions import extensions

# from sqlalchemy import desc, asc, func
# from sqlalchemy import and_, or_
# from flask_socketio import SocketIO, emit
# from datetime import datetime

db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

socketio = extensions.socketio
@home.route('/')
def home_view():
    return render_template('home.html')

