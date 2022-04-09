# blog-back-django
- View = controllers
-  templates = pages
-  static = img + css

* Architecture:
Django uses the MVC (Model-View-Controller) software architecture.

Notice that there is nothing called Controller in our diagram. That is because the naming in the Django architecture is different.

The Model from MVC is Model in Django.
The View from MVC is Template in Django.
The Controller from MVC is View in Django.



* Migrations
Notice that there is a message saying something about unapplied migrations.Django comes with some preconfigured packages that deal with our database. Since we've just gotten these packages we have to apply changes to our database to accommodate for them. This is done by running the migrate command.

* Project Architecture

Let's explain what these files are:

manage.py contains a bunch of commands/options to interact with the Django project in various ways.
db.sqlite3 is the database file that holds the information you will add to your project.
The inner blog/ directory is the actual Python package for our project. Basically it's what makes everything work right and together.
__init__.py is an empty file that tells Python that this directory should be considered a Python package.
settings.py is the settings/configuration for the Django project.
urls.py is the URL declarations for this Django project; a “table of contents” of your Django-powered site.
wsgi.py is a file that allows your project to be deployed. Read more about it here.

* Creating an App
Before creating an app make sure your virtual environment is activated and that you are in your project root folder; that's where you can see manage.py.

The command to create an app is:

$ python manage.py startapp <APP_NAME>
If we're in our blog project and we wanted to create an app called articles, this is what it will look like:

(django_blog)$ python manage.py startapp articles
Let's see the app folder we just created

(django_blog)$ ls
blog       db.sqlite3 manage.py  articles
Every time we create a new app, we need to include it in the INSTALLED_APPS list in our settings.py file. Open your settings.py and find the INSTALLED_APPS list.

INSTALLED_APPS = [
    'django.contrib.admin',

    '<YOUR_APP_NAME>',
]
Make sure you always add your custom apps below the django.contrib apps.

If you do not add your apps to the INSTALLED_APPS list, your Django project will not be able to recognize them.

* App Architecture
This is the folder/directory structure of the app:

We'll explain each of these components briefly:

admin.py is how we associate the app with the admin page.
apps.py is the app's configuration.
migrations is a folder which holds changes that are made to our database for this app.
models.py is how we map our data to the database.
tests.py is where we can run and design tests for our app.
views.py controls the flow of data in our app.
