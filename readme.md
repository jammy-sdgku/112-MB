#install flask environment ----------------------------------------------------------------------------
python3 -m venv venv

#activate environment --------------------------------------------------------------------------------
source venv/bin/activate

#install django ----------------------------------------------------------------------------------------
pip3 install django

#check files installed --------------------------------------------------------------------------------
pip freeze

#start project
django-admin startproject config . -------------------------------------------------------------------

#start App ---------------------------------------------------------------------------------------------
python3 manage.py runserver
(all commands are to be run as above after manage.py)

#create structure for project  
 static folder
templates folderimg
css folder
js folder
gitignore

#modify settings in settings.py

#to create App
python3 manage.py startapp <name of app>

#make sure you create urls.py file inside of the app folder (only if you're going to create vies on it)

#install SQLAlchemy -----------------------------------------------------------------------------------
pip install SQLAlchemy

#site info -------------------------------------------------------------------------------------------
http://127.0.0.1:5000

#Models
After we finish modals in python file, we need to run these two commands:
-makemigrations -> Translation from the models.py into sql part
-migrate -> applies the migrations file into the db

#Database info
http://127.0.0.1:8000/

#soft delete - made to deactivate account without deleting it.
is_active:inactive

# 112-blog

STR:

1. Inside of the mb project and with the venv activated, create the pages app
2. Once the pages app is created, make sure to add the urls.py
3. Create the views for HomePage and AboutPage
4. Link the view to the urls.py (dont forget to also link the urls from pages to the urls inside of config)
5. Create the templates are going to handle the views.
6. Create a base.html blueprint with a navbar and the jinja blocks
7. Add the base to the home and about.html

# 112-MB
