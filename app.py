from flask import Flask, render_template, session, redirect
from functools import wraps
from flask_pymongo import PyMongo
import os


app = Flask(__name__)
app.secret_key = b'\xef\xbeP\x93Xg\xaf\xb6\x80I\xc4\xb0\xc7\xf9\x0bd'

# Database
app.config["MONGO_DBNAME"] = 'user_login_system'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@cluster0-dllo5.mongodb.net/user_login_system?retryWrites=true&w=majority"

mongo = PyMongo(app)

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

