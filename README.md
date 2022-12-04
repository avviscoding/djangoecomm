## Ecom Project

# Do not chnages any static files


# Requirments
    asgiref==3.5.2
    Django==4.1.3
    django-countries==7.4.2
    django-crispy-forms==1.14.0
    django-filter==22.1
    Pillow==9.3.0
    sqlparse==0.4.3
    typing_extensions==4.4.0
    tzdata==2022.6

# Install packages
    pip install -r requirments.txt

# create project
    django-admin startproject mysite

# create app
    python manage.py startapp app

# django default model migrate

- python manage.py migrate

# New model migrate

- python manage.py makemigrations
- python manage.py migrate

# start server
    python manage.py runserver

