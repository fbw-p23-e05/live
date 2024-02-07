# /bin/bash

mkdir course
django-admin startproject config course
cd course

# Or:
# mkdir course
# cd course
# django-admin startproject config .

django-admin startapp notes

# Or:
# python manage.py startapp notes

python manage.py runserver
