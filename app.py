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

category = mongo.db.categories
# Home Page route
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# Browse Page
@app.route('/browse')
def browse():
    return render_template("browse.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)