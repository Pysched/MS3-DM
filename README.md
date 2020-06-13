<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# [Book Shelf](https://bookshelf-dm.herokuapp.com/) - Milestone Project Three

![Book Shelf - Desktop](https://res.cloudinary.com/pysched/image/upload/c_scale,w_898/v1592054964/Bookshelf%20images/Screen_Shot_2020-06-13_at_14.27.53_xykdcy.png)


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

### Project Rational

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
- As a reader I want to leave a rating and or a review of books I've read without taking part in anything else - this was not achieved and is in the to be implemented section
- As a blogger, I want to be able to rate listings that I find so that I can let others know how good/bad they are - this feature was not completed and is part of the future implementation section.
- As a consumer, I want to be able to use a site that is not a direct seller and is not bias towards any one book, publisher or author, in particular


### Style Development

The direction I took for the styling of the site was that of a minimal design theme. The content show do the talking, with the aim of not having too many flashing lights and dominate colours or overtly dynamic elements confusing users as to were to go or how to get around the site. To that end i selected a colour palette that is light and complimentary in colour and based around a pastel style scheme.

The below colour palette are the base from which I selected colours from the site. 

Primary Colour Palette: 

![Primary Colour Palette](https://res.cloudinary.com/pysched/image/upload/v1592048872/Bookshelf%20images/colour_palette_2_xzmk1p.jpg)


Secondary Colour Palette:

![Secondary Colour Palette](https://res.cloudinary.com/pysched/image/upload/v1592048872/Bookshelf%20images/colour_palette1_x6ykem.jpg)




### Wireframes

Wireframes where developed by hand. A personal chocice as I find it a rapid and iterative process for me to develop wireframes where I can quickly modify and change features as I please.  

The links to these images are available at the following links:

- [**_Wireframe 1_**](https://res.cloudinary.com/pysched/image/upload/c_scale,w_898/v1592056245/Bookshelf%20images/CamScanner_05-26-2020_02.05.46_Page_1_ddk1pj.jpg)

- [**_Wireframe 2_**](https://res.cloudinary.com/pysched/image/upload/c_scale,w_898/v1592055981/Bookshelf%20images/CamScanner_05-26-2020_02.05.46_Page_2_rckxsg.jpg)

- [**_Wireframe 3_**](https://res.cloudinary.com/pysched/image/upload/c_scale,w_898/v1592056298/Bookshelf%20images/CamScanner_05-26-2020_02.05.46_Page_3_yujc27.jpg)

- [**_Wireframe 4_**](https://res.cloudinary.com/pysched/image/upload/c_scale,w_898/v1592056377/Bookshelf%20images/CamScanner_05-26-2020_02.05.46_Page_4_texd8j.jpg)


My Final Project design and layout differs from my initial wireframes. This occured as part of my development iteration process. As the site evloved and technoical challenges either become too much or overocme, the design changed to reflect that, the initial wireframes gave me a great base from which to start and develop from and are an essential part of the process. 

### Database Schema

I designed a database schema before starting my project, the layout for these are available here: 
- [**_Database Schema Page 1_**](https://res.cloudinary.com/pysched/image/upload/v1592062758/Bookshelf%20images/Database_Schema_Page_1_lymylj.jpg)
- [**_Database Schema Page 2_**](https://res.cloudinary.com/pysched/image/upload/v1592062758/Bookshelf%20images/Database_Schema_Page_2_jc29mu.jpg)
 -[**_Database Schema Page 3_**](https://res.cloudinary.com/pysched/image/upload/v1592062759/Bookshelf%20images/Database_Schema_Page_3_ny5au8.jpg)
- [**_Database Schema Page 4_**](https://res.cloudinary.com/pysched/image/upload/v1592062758/Bookshelf%20images/Database_Schema_Page_4_ivpzxu.jpg)

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
The testing of users Stories consisted of:

1. Creating a new account - Register functionality
2. Logging out - can the user log out - Logout functionality
3. Log in - can the user log back in - Login functionality
4. Create - Add a listing - can the user add a new listing - Add item Functionality
5. Read - Can a user read their newly added listing - Read functionality 
6. Update - Edit a listing  - can a user edit a listing - Edit listing functionality
7. Delete a listing - can a user delete a listing - Delete listing functionality
8. Feed back - does the user get the flashed messages to provide feedback
9. Create a book club meeting - can a user cerate a book club meeting - Create meeting functionality
10. Read - Can a user read a created book club meeting - Read Meeting Functionality
11. Update - Can a user edit a book club meeting - Edit Meeting Functionality
12. Delete - can a user delete a book CLub meeting - Delete meeting Functionality
13. Read - Can a user read their account information - Read Functionality
14. Update - can a user update their account information - Edit functionality
15. Delete - Can a user delete their account - Delete functionality
16. Navigation Navbar - can a user naviagate the site through full screen navigation at the navbar
17. Naviagtion Footer - can a user navigate the site through the footer

### Responsive and Functional Testing
- I tested my apps responiveness on different size sizes; Mobile, tablet and Desktop to ensure that the responiveness worked and the site is funcitonal at all sizes.
- Tested on Desktop (My Pc)
- Tested on Tablet (Responive desinger in Chrome and Firefox)
- Tested on Mobile (Samsun s10)

### Functionality

For testing of functionality I have tested it myself trying each of the dyna,ic elements on all sizes.

Tesing included:
- Navbar Links
- Logo link
- Cards arrow click for reverse card information
- All buttons on all elements
- Accordian for meetings
- Flashed messages for user feedback
- Footer navigation

### Additional Testing
- I used the developer tools with both Firefox and Chrome to check each of my styling, responiveness and erros with. This ensured that I identified and I was able to modify errors and bugs quickly and on the fly, and bring those edits back into gitpod.

- I created several users and when through each of the available functionality steps, these where:
    - Registering
    - Login
    - Signing out
    - Editing account information
    - Deleting an account
    - Adding a listing
    - Editing a listing
    - Deleting a listing
    - Creating a meeting
    - Editing a meeting
    - Deleting a meeting
    - Navigation links
    - Dropdown Accordians
    - Buttons
    - Links
    - Modals
    - Sidenav for mobile screens
    - Flashed messages for user feedback
    - Footer Navigation

I also asked several family memebers and friends to do the same along the way to capture any issues and debug them as well as providing feedback.


### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

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

[Book Shelf](https://bookshelf-dm.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Book Shelf](https://github.com/Pysched/MS3-DM)

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

- All of the code for my project was written by me.
- I learned and developed my knowledge and understanding of how to implement a user login with encrypted password through reviewing and learning from the following student projects: [**_Student Cook Book Project_**](https://github.com/hebs87/cookbook-milestone-project-three), [**_Student Fitness Pot Project_**](https://github.com/tomciosegal/fitness_pot)
- Using these resources as a reference I was able to craft my own code to perform the desired functionality. 
- I also want to acknowledge the amazing support I recieved from tutor support. They were fantastic in helping me identify issues and teaching me how to resolve them. They are a fantastic resource.
- I got a general idea of how to create a register and login system by watching this [Login Video](https://www.youtube.com/watch?list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&v=vVx1737auSE&app=desktop) and pairing it to the above reference user login methods
- Flash Messages Article [Flash Messages Article](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) This article help me is understand and deploy the flashed messages in the app.


### Content

- The content for the game was created by myself.

### Media

Images used in this project where sourced from royality free locations

[**_Main Site Image_**](https://www.pexels.com/photo/blur-book-stack-books-bookshelves-590493/)

[**_Book Club Image_**](https://media.edutopia.org/styles/responsive_2880px_16x9/s3/masters/2018-08/iStock-487922329_master.jpg)

[**_Browse Image_**](https://images.pexels.com/photos/3769697/pexels-photo-3769697.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)

[**_Register Image_**](https://image.freepik.com/free-photo/girl-holding-book-front-face_23-2147690566.jpg)

The listing item images are added by users from the various sites or locations that the users find images for.


### Acknowledgements

Major thank you to the tutoring team for their invaluable support in guiding me through issues I had. Their method of support is great as they describe the issue and guide you to undersstanding how to resolve issues yourself. fantastic team.

A thank you to my mentor, Rahul Patil, for his review of my project scope and layout.

### Disclaimer

This project is for educational purposes only.
