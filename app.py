import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookshelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-46ezx.mongodb.net/bookshelf?retryWrites=true&w=majority'
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Database reference
users = mongo.db.users
category = mongo.db.categories


# Home Page route
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# Book Club Page
@app.route('/book_club')
def book_club():
    return render_template("book_club.html")


# Browse Page
@app.route('/browse')
def browse():
    return render_template("browse.html")


# Login Page
@app.route('/login', methods=['GET'])
def login():
    # Check is the user in the db and in a session
    if 'user' in session:
        user_reg = users.find_one({"username": session['user']})
        # If the user is in the db redirect to the users account
        if user_reg:
            return redirect(url_for('account', user=user_reg['username']))
    else:
        # If the user is not in the db, redirect them back to the login page
        return render_template("login.html")


# User auth - check login details versus the db details
@app.route('/user_auth', methods=['POST'])
def user_auth():
    form = request.form.to_dict()
    user_reg = users.find_one({"usename": form['username']})
    # Database check for user
    if user_auth:
        # Hashed password - Real Password check
        if check_password_hash(user_reg['password'], form['password']):
            # Add user to session
            session['user'] == form['username']
            return redirect(url_for('account', username=user_reg['username']))
        else:
            flash("Wrong username or password, please enter again!")
            return redirect(url_for('login'))


# Register Page
@app.route('/register')
def register():
    return render_template("register.html")


# Account Page
@app.route('/account')
def account():
    return render_template("account.html")


# Add Item Page
@app.route('/add_item')
def add_item():
    return render_template("add_item.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)