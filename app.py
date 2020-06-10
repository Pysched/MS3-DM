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
meetings = mongo.db.meetings
meeting_category = mongo.db.meeting_category


# Quick functions
def find_user(username):
    return users.find_one({"username": username})


def find_listings(listings_id):
    return listings.find_one({"_id": ObjectId(listings_id)})


def find_meetings(meetings_id):
    return meetings.find_one({"_id": ObjectId(meetings_id)})


# Home Page route
@app.route('/')
@app.route('/index')
def index():
    sci_books = mongo.db.listings.find({'item_category': 'Sci-Fiction'})
    fic_books = mongo.db.listings.find({'item_category': 'Fiction'})
    crime_books = mongo.db.listings.find({'item_category': 'Crime'})
    drama_books = mongo.db.listings.find({'item_category': 'Drama'})
    bio_books = mongo.db.listings.find({'item_category': 'Biography'})
  

    return render_template("index.html", sci_books=sci_books, fic_books=fic_books, crime_books=crime_books, drama_books=drama_books, bio_books=bio_books)


# Book Club Page
@app.route('/book_club', methods=['GET', 'POST'])
def book_club():
    return render_template("book_club.html", meetings=mongo.db.meetings.find(), meetings_category=mongo.db.meetings_category.find(),
    book_category=mongo.db.book_categories.find())


# Add Meetings
@app.route('/add_meeting', methods=['GET', 'POST'])
def add_meeting():
    return render_template('add_meeting.html')


# Add Meetings
@app.route('/insert_meeting', methods=['GET', 'POST'])
def insert_meeting():
   
    if request.method == 'POST':
        
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        today_date = date.today()
        curr_date = today_date.strftime("%d %B %Y")
        insert = {
            "meeting_name": request.form.get("meeting_name"),
            "meeting_date": request.form.get("meeting_date"),
            "meeting_time": request.form.get("meeting_time"),
            "meeting_description": request.form.get("meeting_description"),
            "meeting_category": request.form.get("meeting_category"),
            "meeting_book_category": request.form.get("meeting_category"),
            "meeting_added_by": user_id,
            "meeting_added_by_username": user,
            "meeting_added_date": curr_date,
            "item_removed": False
        }

        new_meetings = meetings.insert_one(insert)
        users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_item": new_meetings.inserted_id}}
        )
        flash(Markup("Success \
                    " + user + ", \
                    your listing has been added!"))

        return redirect(url_for('book_club'))


# Get Meetings
@app.route('/get_meetings', methods=['GET', 'POST'])
def get_meetings():
    return render_template("get_meetings.html",
    listings=mongo.db.listings.find(), book_categories=mongo.db.book_categories.find(),
    meetings=mongo.db.meetings_category.find())


# Get updatepage
@app.route('/get_update_page/<meeting_id>', methods=["GET", "POST"])
def get_update_page(meeting_id):
    meeting = mongo.db.meetings.find_one({'_id': ObjectId(meeting_id)})
    return render_template("sections/edit_meeting.html", meeting=meeting)

# Update Meetings
@app.route('/update_meetings/<meeting_id>', methods=["GET", "POST"])
def update_meetings(meeting_id):
    meeting = mongo.db.meetings
    meeting.update({'_id': ObjectId(meeting_id)}, {
        "meeting_name": request.form.get("edit_meeting_name"),
        "meeting_date": request.form.get("edit_meeting_date"),
        "meeting_time": request.form.get("edit_meeting_time"),
        "meeting_description": request.form.get("edit_meeting_description")
        })
    return redirect(url_for('book_club'))


# Delete Meetings
@app.route('/delete_meeting/<meeting_id>', methods=["GET", "POST"])
def delete_meeting(meeting_id):
    user = session['user']
    meetings = mongo.db.meetings
    meetings.remove({'_id': ObjectId(meeting_id)})
    flash(Markup("Oh Well " + user.capitalize() + ", There'll be no escape for the princess this time!!"))

    return redirect(url_for('book_club'))


# Browse Page
@app.route('/browse', methods=['GET', 'POST'])
def browse():

    return render_template("browse.html", cards=mongo.db.listings.find())


# Get individual listing
@app.route('/listings/<listings_id>', methods=["GET", "POST"])
def listings(listings_id):
    listings = mongo.db.listings.find_one({"_id": ObjectId(listings_id)})
    return render_template('listing.html', listings=listings)


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the request method is post then return then login.html
    if request.method == "POST":
        ''' get the inserted values from the login form and assign them ids of username, password, reg_user'''
        username = request.form.get('username')
        password = request.form.get("user_password")
        reg_user = find_user(username)
        '''check if the reg_user which is the call to the users db and assigned to the varible taken from the login form and check the hashed password vs the stored password'''
        if reg_user and check_password_hash(reg_user["password"], password):
            ''' if they match then login and greet user with message including their name from the database, capitlizing their name, and redirect them to the home page'''
            flash(Markup("Hey, Welcome " 
            + username.capitalize() + 
            ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            ''' else, they details did not match, prompt the user to try again or go and register'''
            flash(Markup("Those details do not match our records, either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('login.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        '''
        If the method is POST, then take the values from the form and assign them to new_nuser, new_pass and new_email, .lower() function is to prevent issues with case sensitive logins later on
        '''

        new_user = request.form.get('new_user').lower()
        new_pass = request.form.get('new_pass')
        new_email = request.form.get('new_email')
        reg_user = find_user(new_user)

        '''# Error handling for the case where a user name is already taken, rediret the form back to register'''

        if reg_user:
            flash(Markup("The username " + new_user + " is already in taken, please try another name"))
            return redirect(url_for('register'))

        '''# If the new_user is not in the database then insert into the user collection in the db the following keys and values from the form, run hash password on the password first and create varibles for arrays to be added to by the user down the road.'''

        users.insert_one({
            "username": new_user,
            "password": generate_password_hash(new_pass),
            "email": new_email,
            "added_listings": [],
            "liked_listings": []
        })

        '''# Add new_user to the session variable user and display a welcome message, redirect the user to the home page/ index page with the session variable being equal to user'''
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


# Edit Profile
@app.route('/edit_profile/<user_id>', methods=["GET", "POST"])
def edit_profile(user_id):
    the_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('edit_profile.html', user=the_user)


# Update Profile
@app.route('/update_profile/<user_id>', methods=["GET", "POST"])
def update_profile(user_id):
    users = mongo.db.users
    new_pass = request.form.get('new_pass')
    users.update_many({'_id': ObjectId(user_id)}, {
        'username': request.form.get('new_user'),
        "password": generate_password_hash(new_pass),
        "email": request.form.get('new_email'),
        "add_item": []
    })
    return redirect(url_for('logout'))


# Delete Profile
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = session['user']
    mongo.db.user_id.delete_one({'_id': ObjectId(user_id)})
    session.clear()
    flash(Markup("Sorry to see you go.." "Good Bye"))
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
    '''
    From the add_item page take the selected inputs for a new item and insert it into the database referencing the user that added it
    '''
    if request.method == 'POST':
        '''# Get the current users session, and date from today function and display it as date number, month name and year '''
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        today_date = date.today()
        curr_date = today_date.strftime("%d %B %Y")
        '''# Insert the values from the form with the key values on the left into the listings collection, to be able to select items from the db add a boolean of false to item_removed, this will be used further fown the script to call all items with a False value'''
        insert = {
            "item_type": request.form.get("item_type"),
            "item_title": request.form.get("item_title"),
            "item_author": request.form.get("item_author"),
            "item_read_time": request.form.get("item_read_time"),
            "item_category": request.form.get("item_category"),
            "item_rating": request.form.get("item_rating"),
            "item_comment": request.form.get("item_comment"),
            "item_added_by": user_id,
            "item_added_by_username": user,
            "item_added_date": curr_date,
            "item_likes": 0,
            "item_removed": False,
            "item_url": request.form.get("item_url")
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


# Delete Item
@app.route('/remove_listing/<listings_id>')
def remove_item(listings_id):
    user = session['user'].lower()
    mongo.db.listings.remove({'_id': ObjectId(listings_id)})
    flash(Markup("Thanks " + user.capitalize() + " this listings has been successfully deleted!"))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)