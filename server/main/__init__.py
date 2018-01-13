from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash, render_template

from flask import session as login_session

from main.models import Base, Seller, Client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps

import random, string

import flask_login
from flask_login import LoginManager, login_user

# from itsdangerous import URLSafeTimedSerializer

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

#===================== INIT CODE ============================

engine = create_engine('sqlite:///site.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.secret_key = "userloginapplication"
app.debug = True

# server = smtplib.SMTP('smtp.gmail.com', 587)

# ================= BEGIN LOGIN REQUIREMENT CODE ==============

@login_manager.user_loader
def load_user(user_id):
    '''
    Takes a unicode format user id and uses it to retrieve the respective user
    object to be used by the login_manager
    '''
    try:
        user = session.query(Seller).filter_by(id=int(user_id)).first()
    except:
        user = session.query(Client).filter_by(id=int(user_id)).first()

    return user

# ================== END LOGIN REQUIREMENT CODE ===============

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    # REQUEST URL:
    # https://www.dineoncampus.com/v1/location/menu.json?date=2018-01-13T03:00:59.764Z&location_id=5877ad223191a20074d827dc&platform=0&site_id=5751fd2b90975b60e0489294
    # mess with the 'date' parameter to get menu for specific days
    return return_template('menu.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return "This is where users will signup"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "This is where users will login"

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return url_for(index)

@app.route('/<user>/profile', methods=['GET', 'POST'])
def view_profile(user):
    return "This is where users can view their profile"

@app.route('/<user>/profile/edit', methods=['GET', 'POST'])
def edit_profile(user):
    return "This is where users can edit their profile"

@app.route('/<user>/requests_sent', methods=['GET', 'POST'])
def view_sent_requests(user):
    return "This is where a user can see the requests they've sent to other users"

@app.route('/<user>/requests_received', methods=['GET', 'POST'])
def view_received_requests(user):
    return "This is where a user can see the requests they've received from other users"

@app.route("/search", methods=['GET', 'POST'])
def search():
    return "This is where search results will appear"

@app.route("/search/<selected_user>", methods=['GET', 'POST'])
def user_searched(selected_user):
    return "This is where information about the user clicked on from searching will appear"

@app.route("/search/<selected_user>/request", methods=['GET', 'POST'])
def request_user(selected_user):
    return "This is where users can request another user to sell to/buy from"
