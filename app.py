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
    # if the request method is post then return then login.html 
    if request.method == "POST":
        # get the inserted values from the login form and assign them ids of username, password, reg_user
        username = request.form.get('username')
        password = request.form.get("user_password")
        reg_user = find_user(username)
        # check if the reg_user which is the call to the users db and assigned to the varible taken from the login form and check the hashed password vs the stored password
        if reg_user and check_password_hash(reg_user["password"], password):
            # if they match then login and greet user with message including their name from the database, capitlizing their name, and redirect them to the home page
            flash(Markup("Hey, Welcome " 
            + username.capitalize() + 
            ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            # else, they details did not match, prompt the user to try again or go and register
            flash(Markup("Those details do not match our records, either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('login.html')
  

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        # If the method is POST, then take the values from the form and assign them to new_nuser, new_pass and new_email, .lower() function is to prevent issues with case sensitive logins later on
        new_user = request.form.get('new_user').lower()
        new_pass = request.form.get('new_pass')
        new_email = request.form.get('new_email')
        reg_user = find_user(new_user)

        # Error handling for the case where a user name is already taken, rediret the form back to register
        if reg_user:
            flash(Markup("The username " + new_user + " is already in taken, please try another name"))
            return redirect(url_for('register'))

        # If the new_user is not in the database then insert into the user collection in the db the following keys and values from the form, run hash password on the password first and create varibles for arrays to be added to by the user down the road.
        users.insert_one({
            "username": new_user,
            "password": generate_password_hash(new_pass),
            "email": new_email,
            "added_listings": [],
            "liked_listings": []
        })

        # Add new_user to the session variable user and display a welcome message, redirect the user to the home page/ index page with the session variable being equal to user
        session["user"] = new_user
        flash(Markup("Welcome aboard, " + new_user.capitalize() + "<br>" + "You're now part of the team, and logged in!"))

        return redirect(url_for('index', username=session["user"]))


    return render_template("register.html")


# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.pop('user', None)
    flash('You\'re outta here!')
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
    # Return the add_item page and call the items from the following collections to populate the dropdown fields
    return render_template("add_item.html", 
    items=mongo.db.items.find(), 
    reading=mongo.db.item_read_time.find(),
    book_cat=mongo.db.book_categories.find(), 
    rating=mongo.db.item_rating.find())


# Insert Item
@app.route('/insert_item', methods=["GET", "POST"])
def insert_item():
   
    # From the add_item page take the selected inputs for a new item and insert it into the database referencing the user that added it
    
    if request.method == 'POST':
        # Get the current users session, and date from today function and display it as date number, month name and year 
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        today_date = date.today()
        curr_date = today_date.strftime("%d %B %Y")
        # Insert the values from the form with the key values on the left into the listings collection, to be able to select items from the db add a boolean of false to item_removed, this will be used further fown the script to call all items with a False value
        insert = {
            "item_type": request.form.get("item_type"),
            "item_title": request.form.get("item_title"),
            "item_author": request.form.get("item_author"),
            "item_read_time": request.form.get("item_read_time"),
            "item_category": request.form.get("item_category"),
            "item_rating": request.form.get("item_rating"),
            "item_added_by": user_id,
            "item_added_by_username": user,
            "item_added_date": curr_date,
            "item_likes": 0,
            "item_removed": False
        }

        new_listing = listings.insert_one(insert)

        users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_item": new_listing.inserted_id}}
        )
        flash(Markup("Success \
                    " + user + ", \
                    your listing has been added!"))

        return redirect(url_for('browse'))


@app.route('/get_listings', methods=["GET, POST"])
def get_listings():

    if request.method == 'POST':
        user_submit = request.form.to_dict()
        listings = listings.find({"item_removed": False})

    return render_template("browse.html", listings=listings.find())


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)