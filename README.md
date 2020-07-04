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


