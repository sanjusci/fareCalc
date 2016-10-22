Requirements
   Python (2.7, 3.2, 3.3, 3.4, 3.5)
   Django (1.8, 1.9, 1.10)

Installation

Install using pip...

pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = (
    ...
    'rest_framework',
)
Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

pip install django
pip install djangorestframework
django-admin.py startproject example .
./manage.py migrate
./manage.py createsuperuser

