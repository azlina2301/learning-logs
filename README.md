# Lessons: Django Framework (Project Learning log)
In this lesson, I am learning about the Django Framework by creating a project named Learning Logs.


## Step 1: Create a virtual environment
``` python -m venv ll_venv ```
- We use the venv module to create a virtual environment named ll_venv.

## Step 2: Install the django package
pip install django

## step 3: Setup the project
``` django-admin startproject ll_project . ```
- The startproject command sets up the project named ll_project. The dot (.) after the project name is important it tells Django to create the project with directory structure.
- This command automatically creates manage.py and ll_project folder.
- manage.py is a short program that run a commands and feed the information based on django needed.
- Inside ll_project folder consists of 4 files but there are 3 important files (setting.py, urls.py, wsig.py)
    * settings.py    -> Tell the django to interact with our system an managing the project.
    * urls.py       -> Tell the django what page to build in response to the browser request.
    * wsig.py       -> Help django serve the file it creates.

## Step 4: Creating a database
``` python manage.py migrate ```
- This command is needed whenever we make a change in database. For the first time running this command is used to ensure that the database matches the current state of the project.
- This part will auto create the SQLite db.

## Step 5: Viewing the project
``` python manange.py runserver ```

## Step 6: Start the app
``` python manage.py startapp app_name ```
e.g: ``` python manage.py startapp learning_logs ```
- The startapp app_name command tell the django to create the infrastructure for app building.
- In the project directory, new learning_logs folder is created and consists of admin.py, models.py and views.py
- models.py module is where we define how the django should interact with data.

    ### Defining the model
    - In the models.py we can define new class that represent our data table with inherited from parent class Model.
    - Once we defined the new class we need to migrate this in order the database matches the current state of project.
        ``` python manage.py makemigrations learning_logs
            python manage.py migrate
        ```
    - We need to tell django to include this by include the app in setting.py

## Step 7: Making the page
- Making web pages with django consists of 3 stages.
    * Defining the URL.         -> Describe the way URL is laid out. Tell the django what to look for when matching the browser request and url site. Then map with views.
    * Writing the views.        -> The views function retrieve and processing the data based on the browser request and render to the template.
    * Writing the templates.    -> The template consists of overall structures.s