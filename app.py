import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo
from datetime import date
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
listings = mongo.db.listings
items = mongo.db.items


# Quick functions
def find_user(username):
    return users.find_one({"username": username})


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
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template("browse.html", listings=mongo.db.listings.find())


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check is the user in the db and in a session
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("user_password")
        reg_user = find_user(username)

        if reg_user and check_password_hash(reg_user["password"], password):

            flash(Markup("Hey, Welcome " 
            + username.capitalize() + 
            ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            flash(Markup("Those details do not match our records, either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('login.html')
  

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
                flash(Markup(f"{form['new_username']} already exists!"))
                return redirect(url_for('register'))
            # If user does not exist register new user
            else:
                # Hash password
                hash_pass = generate_password_hash(form['new_password'])
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
                    return redirect(url_for('index'))
                else:
                    flash(Markup("There was a problem saving your profile"))
                    return redirect(url_for('register'))

        else:
            flash(Markup("Passwords dont match!"))
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
        # if the user is in session return profile.html for that user
        user_in_db = users.find_one({"username": username})
        return render_template('profile.html', user=user_in_db)
    else:
        return redirect(url_for('index'))


# Add Item Page
@app.route('/add_item')
def add_item():
    return render_template("add_item.html", 
    items=mongo.db.items.find(), 
    reading=mongo.db.item_read_time.find(),
    book_cat=mongo.db.book_categories.find(), 
    rating=mongo.db.item_rating.find())


# Insert Item
@app.route('/insert_item', methods=["GET", "POST"])
def insert_item():
    '''
    From the add_item page take the selected inputs for a new item and insert it into the database referencing the user that added it
    '''
    if request.method == 'POST':
        # Get the current users session
        user = session['user']
        user_id = find_user(user)["_id"]

        insert = {
            "item_type": request.form.get("item_type"),
            "item_title": request.form.get("item_title"),
            "item_author": request.form.get("item_author"),
            "item_read_time": request.form.get("item_read_time"),
            "item_category": request.form.get("item_category"),
            "item_rating": request.form.get("item_rating"),
            "item_added_by": request.form.get("item_added_by")
        }

        new_listing = listings.insert_one(insert)

        users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_item": new_listing.inserted_id}}
        )
        flash(Markup("Success \
                    " + user + ", \
                    your listing has been added!"))

        return redirect(url_for('index'))


# Get Listings
# @app.route('/get_listings')
# def get_listings():
#     if request.method == 'POST':
#         return render_template('browse.html', listings=mongo.db.listings.find())





if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)