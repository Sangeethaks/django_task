# django_task

The whole idea is to design and implement a Django application with User and ActivityPeriod models with a custom management command to populate the database with a dummy data. 
And also, to design an API in-order to serve that data in the json format.

## Installation

Install Django itself:
```bash
pip install django
```
let’s set up Django REST Framework JSON API ,so that we can access it via a web service.

Install the following dependencies.
```bash
$ pip install djangorestframework
$ pip install djangorestframework-jsonapi
$ pip install django-filter
```
Project Structure:
```bash
django_task/
  ├──db.sqlite3
  ├── manage.py
  ├──django_task/
  |     ├── __init__.py
  |     ├── urls.py
  |     ├── settings.py
  |     ├── wsgi.py
  ├──myapp/
    |  ├── fixtures/
    |     └── testing_data.json
    |  ├── migrations/
    |     └── __init__.py
    |     └──0001_initial.py
    |
    ├── __init__.py
        ├── apps.py
        ├── models.py
        ├── views.py
        ├── admin.py
        ├── serializers.py
        ├── tests.py
 
```

## Usage

Start the Django server:

```python
$ python manage.py runserver
```

Launch the localhost in any web browser, (http://127.0.0.1:8000/)
And we will be able to see the below results,
```python
GET /

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/vnd.api+json
Vary: Accept

{
    "data": {
        "user": "http://127.0.0.1:8000/user/",
        "activityperiod": "http://127.0.0.1:8000/activityperiod/"
    }
}
```
## Models:
```
"user": "http://127.0.0.1:8000/user/",
"activityperiod": "http://127.0.0.1:8000/activityperiod/"
```
The data from the json file will get displayed in the above server links.
Apart from that, I have designed the script in such a way that we can populate random data using REST API.


## urls.py

In the *"django_task/urls.py"* , I have added the following, 
```python
from django.urls import include, path
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'activityperiod', views.ActivityPeriodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
This will hook up all necessary URLs for the USER and ACTIVITYPERIOD models.
```
GET /user/ — lists all the users          -----  Ex: "http://127.0.0.1:8000/user/"
GET /user/:id — gets one user             -----  Ex: "http://127.0.0.1:8000/user/123"
DELETE /user/:id — deletes a user  
```
