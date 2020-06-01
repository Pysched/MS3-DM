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
    user_reg = users.find_one({"username": form['username']})
    # Check for user in database
    if user_reg:
        # If passwords match (hashed / real password)
        if check_password_hash(user_reg['password'], form['user_password']):
            # Log user in (add to session)
            session['user'] = form['username']
            # If the user is admin redirect him to admin area
            if session['user'] == "admin":
                return redirect(url_for('admin'))
            else:
                flash("You were logged in!")
                return redirect(url_for('index', username=user_reg['username']))
        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('index'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actual;y match
        if form['new_password'] == form['new_password1']:
            # Find user in db
            user = users.find_one({"username": form['new_username']})
            if user:
                flash(f"{form['new_username']} already exists!")
                return redirect(url_for('register'))
            # If user does not exist register new user
            else:
                # Hash password
                hash_pass = generate_password_hash(form['password'])
                # Create new user with hashed password
                users.insert_one(
                    {
                        'username': form['new_username'],
                        'email': form['new_email'],
                        'password': hash_pass
                    }
                )
                # Check if user is in db
                user_reg = users.find_one({"username": form['new_username']})
                if user_reg:
                    # Add to session
                    session['user'] = user_reg['username']
                    return redirect(url_for('account', user=user_reg['username']))
                else:
                    flash("There was a problem saving your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html")


# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('index'))


# Account Page
@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username): 
    # Check if user is logged in
    if 'user' in session:
        # if the user is in session return profile.html
        user_in_db = users.find_one({"username": username})
        return render_template('profile.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('index'))


# Add Item Page
@app.route('/add_item')
def add_item():
    return render_template("add_item.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)