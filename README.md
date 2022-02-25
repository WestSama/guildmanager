## My Final Project submission for CS50W : Web Programming with Python and Javascript

### What is my project?

- For my project I decided to build a Guild Manager App, for a long time i have been playing Online games and wished that one day if i could build a web app to help my Guild i would do it. Since i can remember we been managing our guild members with Excel Sheets or other type of sheet online. With this app i made this process more simple and interactive with also extra features that guild members can use.

- This project is build with Django as backend and HTML/CSS/JavaScript/Bootstrap 5 Admin DashBoard in the frontend.

- Your guild members are able to create their own account and add their character to the WebApp choose their class and item level will automatically add image to the respective class, they can check current guild members and staff, only staff member have access to the admin panel where they can choose what guild the character will go, also have access a gallery to showcase your best achievements in the game.

### Installation:

- Run first requirements.txt by typing in the terminal: pip install -r requirements.txt
- Make migrations by doing: python manage.py makemigrations and apply them with: python manage.py migrate
- Create a superuser by typing python manage.py createsuperuser
- Now what's left is run the server: python manage.py runserver
- Go to your localhost to enter the website


### What contains in the app and what is it for?

- Main folder
 - static/images - This is where all images from the gallery are uploaded to.
 - guildmanager - Where the base settings, like media root and static root, apps are.
 - manage.py - To initialize the app

 - Guildboard - Where everything done in the app is.
    - static/guildboard/assets/img - Where the image for each class character are when we choose what class we add and Logo.
    - css/styles.css - Bootstrap css
    - js/datatables.js - Script to run the datatable that shows the guild members, runs in guild.html
    - js/imagepreview.js - Previews the image when adding new image to gallery, runs in gallery.html
    - scripts.js - Sidebar toggle, runs in all app

    - templates/guildboard
        - addcharacter.html - Page to add a character
        - addimage.html - Page to add a image to the gallery
        - gallery.html - Shows all images that are upload in the app
        - guild.html - Show the table with all guild members
        - index.html - Main page that shows your characters
        - layout.html - Layout of the web app
        - login.html - Login page
        - register.html - Register page
        - updatechar.html - Page to update the character info
        - viewimage.html - Shows image clicked by user in bigger view

    - admin.py - Shows the models in the admin panel
    - forms.py - Contains the forms used to Update character and create a user
    - models.py - All models used in the app,
        - Class model - Stores all classes of the current game
        - Guild model - All guild names
        - Character model - Stores all information about character
        - Image model - All information about the images that are uploaded in the webapp
    - urls.py - All the routes/urls used
    - views.py - All the views code and backend logic

 Project video showcase: 
