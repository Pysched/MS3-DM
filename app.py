import os
from flask
import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bookshelf'
app.mongo_uri = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

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
    real_books = mongo.db.listings.find({'item_category': 'Real Life'})
    doc_books = mongo.db.listings.find({'item_category': 'Documents'})
    non_books = mongo.db.listings.find({'item_category': 'Non-Fiction'})
    col_books = mongo.db.listings.find({'item_category': 'Collections'})
    return render_template(
        "index.html",
        sci_books=sci_books,
        fic_books=fic_books,
        crime_books=crime_books,
        drama_books=drama_books,
        bio_books=bio_books,
        real_books=real_books,
        doc_books=doc_books,
        non_books=non_books,
        col_books=col_books)


# Book Club Page
@app.route('/book_club', methods=['GET', 'POST'])
def book_club():
    meetings = mongo.db.meetings.find()
    meetings_category = mongo.db.meetings_category.find()
    book_category = mongo.db.book_categories.find()
    return render_template(
        "book_club.html",
        meetings=meetings,
        meetings_category=meetings_category,
        book_category=book_category)


# Add Meetings
@app.route('/add_meeting', methods=['GET', 'POST'])
def add_meeting():
    meetings = mongo.db.meetings.find()
    meetings_category = mongo.db.meetings_category.find()
    book_category = mongo.db.book_categories.find()
    return render_template(
        'add_meeting.html',
        meetings=meetings,
        meetings_category=meetings_category,
        book_category=book_category)


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
    return render_template(
        "get_meetings.html",
        listings=mongo.db.listings.find(),
        books=mongo.db.book_categories.find(),
        meetings=mongo.db.meetings_category.find())


# Get updatepage for meetings
@app.route('/get_update_page/<meeting_id>', methods=["GET", "POST"])
def get_update_page(meeting_id):
    meeting = mongo.db.meetings.find_one({'_id': ObjectId(meeting_id)})
    return render_template("edit_meeting.html", meeting=meeting)

# Update Meetings function
@app.route('/update_meetings/<meeting_id>', methods=["GET", "POST"])
def update_meetings(meeting_id):
    user = session['user'].lower()
    user_id = find_user(user)["_id"]
    today_date = date.today()
    curr_date = today_date.strftime("%d %B %Y")
    meeting = mongo.db.meetings
    meeting.update({'_id': ObjectId(meeting_id)}, {
        "meeting_name": request.form.get("edit_meeting_name"),
        "meeting_date": request.form.get("edit_meeting_date"),
        "meeting_time": request.form.get("edit_meeting_time"),
        "meeting_description": request.form.get("edit_meeting_description"),
        "meeting_added_by": user_id,
        "meeting_added_by_username": user,
        "meeting_added_date": curr_date
        })
    return redirect(url_for('book_club'))


# Delete Meetings
@app.route('/delete_meeting/<meeting_id>', methods=["GET", "POST"])
def delete_meeting(meeting_id):
    user = session['user']
    meetings = mongo.db.meetings
    meetings.remove({'_id': ObjectId(meeting_id)})
    flash(Markup(
        "Oh Well " + user.capitalize() +
        ", There'll be no escape for the princess this time!!"))

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
        # Get form elemnts
        username = request.form.get('username')
        password = request.form.get("user_password")
        reg_user = find_user(username)
        # User and password check
        if reg_user and check_password_hash(reg_user["password"], password):
            # Confirmation message
            flash(Markup(
                "Hey, Welcome "
                + username.capitalize() +
                ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            # Login validation
            flash(Markup(
                "Those details do not match our records," +
                "either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('login.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Add new user, lower case the name for access logic

        new_user = request.form.get('new_user').lower()
        new_pass = request.form.get('new_pass')
        new_email = request.form.get('new_email')
        reg_user = find_user(new_user)

        # Error handling

        if reg_user:
            flash(Markup(
                "The username " + new_user +
                " is already taken, please try another name"))
            return redirect(url_for('register'))

        # insert items to the database
        users.insert_one({
            "username": new_user,
            "password": generate_password_hash(new_pass),
            "email": new_email,
            "added_listings": [],
            "liked_listings": []
        })

        # Add new_user to session and display message
        session["user"] = new_user
        flash(Markup("Welcome aboard, "
                     + new_user.capitalize() +
                     "<br>" +
                     "You're now part of the team, and logged in!"))

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
    users.update({'_id': ObjectId(user_id)}, {
        'username': request.form.get('new_user'),
        "password": generate_password_hash(new_pass),
        "email": request.form.get('new_email'),
        "add_item": []
    })
    return redirect(url_for('logout'))


# Delete Profile
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = session['user'].lower()
    byeuser = mongo.db.users
    byeuser.remove({'_id': ObjectId(user_id)})
    session.clear()
    flash(Markup(
        user.capitalize() + " Has left the building ... Good Bye"))
    return redirect(url_for('index'))

# Add Item Page
@app.route('/add_item')
def add_item():
    # add item and ref db categories for select items
    items = mongo.db.items.find()
    reading = mongo.db.item_read_time.find()
    book_cat = mongo.db.book_categories.find()
    rating = mongo.db.item_rating.find()
    return render_template(
        "add_item.html",
        items=items,
        reading=reading,
        book_cat=book_cat,
        rating=rating)

# Insert Item
@app.route('/insert_item', methods=["GET", "POST"])
def insert_item():
    # Add item to db
    if request.method == 'POST':
        # Get user, date, time and form items insert to db
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        today_date = date.today()
        curr_date = today_date.strftime("%d %B %Y")
        listing = mongo.db.listings
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
            "item_url": request.form.get("item_url"),
            "item_purchase": request.form.get("item_purchase")
        }
        new_item = listing.insert_one(insert)
        # add user id to insert item
        users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_item": new_item.inserted_id}}
        )
        flash(Markup("Success \
                    " + user + ", \
                    your listing has been added!"))

        return redirect(url_for('browse'))

# Get updatepage
@app.route('/get_update_listing/<listings_id>', methods=["GET", "POST"])
def get_update_listing(listings_id):
    listings = mongo.db.listings
    items = mongo.db.items.find()
    reading = mongo.db.item_read_time.find()
    book_cat = mongo.db.book_categories.find()
    rating = mongo.db.item_rating.find()
    listings = mongo.db.listings.find_one({'_id': ObjectId(listings_id)})
    return render_template(
        "edit_listing.html",
        listings=listings,
        items=items,
        reading=reading,
        book_cat=book_cat,
        rating=rating)


# Update Listings
@app.route('/update_listing/<listings_id>', methods=["POST"])
def update_listing(listings_id):
    user = session['user'].lower()
    user_id = find_user(user)["_id"]
    today_date = date.today()
    curr_date = today_date.strftime("%d %B %Y")
    listings = mongo.db.listings
    listings.update({'_id': ObjectId(listings_id)}, {
        "item_type": request.form.get("edit_item_type"),
        "item_title": request.form.get("edit_item_title"),
        "item_author": request.form.get("edit_item_author"),
        "item_read_time": request.form.get("edit_item_read_time"),
        "item_category": request.form.get("edit_item_category"),
        "item_rating": request.form.get("edit_item_rating"),
        "item_comment": request.form.get("edit_item_comment"),
        "item_added_by": user_id,
        "item_added_by_username": user,
        "item_added_date": curr_date,
        "item_likes": 0,
        "item_removed": False,
        "item_url": request.form.get("edit_item_url"),
        "item_purchase": request.form.get("edit_item_purchase"),
        })
    return redirect(url_for('browse'))

# Delete Item
@app.route('/remove_listing/<listings_id>')
def remove_listing(listings_id):
    user = session['user'].lower()
    listing = mongo.db.listings
    mongo.db.listings.remove({'_id': ObjectId(listings_id)})
    flash(Markup("Thanks "
                 + user.capitalize() +
                 " this listings has been successfully deleted!"))

    return redirect(url_for('browse'))


if __name__ == '__main__':
    
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)