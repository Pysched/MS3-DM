<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">
# [Book Shelf](https://bookshelf-dm.herokuapp.com/) - Milestone Project Three

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Development](#Style-Development)
  - [Wireframes](#Wireframes)
  - [Database Schema](#Database-Schema)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
    - [Resolved Bugs](#Resolved-Bugs)
    - [Partially Resolved or Unresolved Bugs](#Partially-Resolved-or-Unresolved-Bugs)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

Book Shelf is an web application, designed as a great place for avid book lovers, page turners, friendly discussion and a facility to aid users to buy books. The aims of the site are to be a central location for people who want to read reviews by fellow book enthusists, join a bookclub group, arrange online meeting times for healthy discussion and as a place where they can link to buy the books they want.

Users will be able to perform CRUD (Create, Read, Update and Delete) profiles, book listings and book club meetings. Users will be able to update all listings and meetings once they are signed up and logged in.

A free to join site that brings people together and allows them to share their passion and buy books

### Project Rational?

This app was created for the Data Centric Development project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses **CRUD** operations to allow users to easily create, read, update and delete data from a database viewed through a web application

This was developed as both a front-end and backend project. The technologies used for each are:
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, MongoDB
- Hosting: Heroku
- Database: MongoDB

## UX

### User Stories

- As an avid reader of books, I often find myself on the look out for my next book and would like a place that can provide reviews on books not based from a seller site
- As a reader of books who enjoys discussing the books that I read, I would like to find a community that I can join to talk about books online and where I can organise meetings
- As a busy person I want to find a site where I can find reading listings that are not related to a marketing stragey and are based on person opinions
- As a new reader I want to search books in an easy to navigate manner where I can link to the seller site 
- As a community member I want a place where I can view recommendations from other users
- As a reader I want to leave a rating and or a review of books I've read without taking part in anything else
- As a blogger, I want to be able to rate listings that I find so that I can let others know how good/bad they are
- As a consumer, I want to be able to use a site that is not a direct seller and is not bias towards any one book, publisher or author, in particular


### Style Development

The direction I took for the styling of the site was that of a minimal design theme. The content show do the talking, with the aim of not having too many flashing lights and dominate colours or overtly dynamic elements confusing users as to were to go or how to get around the site. To that end i selected a colour palette that is light and complimentary in colour and based around a pastel style scheme.

The below colour palette are the base from which I selected colours from the site. 

Primary Colour Palette: 

(https://res.cloudinary.com/pysched/image/upload/v1592048872/Bookshelf%20images/colour_palette_2_xzmk1p.jpg)


Secondary Colour Palette:

(https://res.cloudinary.com/pysched/image/upload/v1592048872/Bookshelf%20images/colour_palette1_x6ykem.jpg)




### Wireframes

Wireframes where developed by hand. A personal chocice as I find it a rapid and iterative process for me to develop wireframes where I can quickly modify and change features as I please.  

The links to these iamges are available at the following links:


### Database Schema

I designed a database schema before starting my project, the layout for these are available below:

## Features

### Functionality

This app makes use of Python logic to enable users to login and, or register for an account. 
The CRUD features that are available through using Python and Mongodb allow users to create, read, update and delete records in a variety of manners:

- Create book listing
- Create a book club meeting
- Create a user account
- Read their book listings
- Read book listings
- Read/view book listings by all users
- Read Book Club meetings 
- Update their listings
- Update their account
- Update a book club meeting
- Delete a book listing
- Delete book Club meetings
- Delete their user account


### Existing Features

-**Navbar Links** 
The navbar contains the following links to all users:

-- Branding Icon( Also home button )
-- Home Button
-- Book Club button
-- Browse Categories dropdown( Genre, Reviews, Releases, Book of the month ) 
-- Login
-- Register

When the user is registered and logged in, the navbar will add buttons for:
Account, Add Item and log out to the navbar and remove login and register buttons from the UI.

- **Navbar Links logged in**
The following are the nav bar links when a user is logged in:

-- branding Icon (Also a home button)
-- Home Button
-- Book Club button
-- Browse button
-- Account Button (to take the user to their specific account page)
-- Add Item Button ( this feature is only available to registered users to be able to add listings)
-- Log


- **Login** - Facility for previously registered users to login to their account. Authorization checks are used to check that the username and password ( password is hashed ) with the details checked against the stored values in the database before users are logged in.

- **Register** - Facility to allow new users to register for an account. Checks are in place to ensure that the username doesn't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes.

- **Edit Account Details** - Assuming a user exists, then the user will have the facility to update their user profile account details.

- **Cancel Edit** - This feature allows the user to change their mind and return to the their specific profile page.

- **Delete Account** - Facility to allow user to delete their account. This will perform the aciton of removing the entire set of user details from the database, as the users have added listings, I decided to leave the previously added listings by the user, so that their listings are still available to other users

- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar. Upon clicking the button, the user session ends.

- **Browse** - The browse page has a list of all the added listings by all users. 

- **Add Book Listing** - Feature is only available to users who are logged in. Once they are logged in they can add a book listing in this form page. This listing data is then posted to the mongodb database for retrival in the browse and index pages.

- **Cancel Edit** - This feature allows the user to change their mind and return to the index page and continue navigating the site.

- **Edit Book Listing** - This feature allows registered and logged in users to edit book listings. This action removes the selected listing values from the database.

- **Cancel Edit** - This feature allows the user to change their mind and return to the listing page of the specific book listing that they had selected.

- **Remove Book Listing** - This feature allows registered and logged in users to delete book listings. This action removes the selected listing values from the database and returns users to the browse page.

- **Cancel Remove** - This feature allows the user to change their mind and return to the listing page of the specific book listing that they had selected.

- **Add New Book Club Meeting** - A facility for registered and logged in users to add a book club meeting. This information is stored in the databse and consists of user_id, date and time pickers and when the meeting was added. 

- **Edit Book Meeting** - This feature allows users to update the book club meetings. If editing, the user, who must be registered and logged in, can ammend the book club meeting. 

- **Cancel Edit** - This feature allows the user to change their mind and return to the meetings page of all the listed book club meetings.

- **Remove Book Meeting** - This feature allows users to  and delete the book club meeting that they have selected. If deleting, the user, who must be registered and logged in, can delete the book club meeting. 

- **Cancel Remove** - This feature allows the user to change their mind and return to the meeting page of the specific book club meeting that they had selected.


### Features Left to Implement

- **Like Listing** - It was invisioned at the start of the project to add a feature for users to like book listings. To that end I began the profile setup python code with a 'liked listings' array that is created for each user,  with the intention of adding each listing id that the user liked to that array for call back on the profile page. This is a feature I would add in the future.

- **Rate Listing** - It was invisioned at the start of the project to add a feature for users to rate book listings. To that end I began the profile setup python code with a 'rate listings' array that is created for each user,  with the intention of adding each listing id that the user rated to that array for call back on the profile page. Later I would like to develop out the rating feature to give an average rating based on all likes against a listing id and display that average as a number or star icons on each listing.

- **Filter/ Browse By Listing Feature**  - It was invisioned at the start of the project to add a filter/browse by feature for users to search book listings by. 

- **Add Reviews**  - It was invisioned at the start of the project to add a filter/browse by feature for users to search book listings by. I would like to implement this feature in the future.

- **Pagination** - I had hoped to develop a pagination system for all the lisitngs to be more easily browsed and viewed, however time constraints at the end ment this feature is left in the features left to implement section.

- **Blueprints** - Having reviewed other students projects, I came to learn of blueprints and how that package can be used to seperate out various sections of code and reference then in a master py file, while I feel this would have helped greatly in terms of keeping my coding logic together in chunks of features I was unable to dedicate the time to learning how to implement this properly as such it is someting to be learned and added at a later date, or for future proejcts.


## Technologies Used

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - This project makes use of **HTML** as the main structural element of the app.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**Gitpod**](https://gitpod.com)
    - The project has been developed in the gitpod IDE.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project and pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Testing User Stories


### Responsive and Functional Testing


### Additional Testing


### Code Validation

- I will use the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I will use the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I will use the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I will use the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a <app-name>```

6. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

    ```echo web: python <fileName.py> > Procfile```

8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Ran the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```


The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Book Shelf] (https://bookshelf-dm.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Book Shelf] (https://github.com/Pysched/MS3-DM)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository]
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Create a new Database in MongoDB  
9. Create collections 
9. Navigate to the `.bashrc` terminal and add your MongoDB URI in the following format:

    ```MONGO_URI="insert your mongo uri details here"```

10. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
11. You should now be able to run the app locally using the `python3 run.py` command.

## Credits


### Content


### Media

Images used in this project where sourced from royality free locations

Main Site Image - (https://www.pexels.com/photo/blur-book-stack-books-bookshelves-590493/)

Book Club Image - https://media.edutopia.org/styles/responsive_2880px_16x9/s3/masters/2018-08/iStock-487922329_master.jpg

Browse Image -https://images.pexels.com/photos/3769697/pexels-photo-3769697.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260

Register Image - https://image.freepik.com/free-photo/girl-holding-book-front-face_23-2147690566.jpg

The listing item images are added by users from the various sites or locations that the users find images for.


### Acknowledgements


### Disclaimer

This project is for educational purposes only.
