# python-drf-test-task

This is the repository for python-drf-test-task, which performs all the tasks from the ToR and additional ones.

![title](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/1.gif)

### Diagram DB

![Diagram](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/diagramDB.svg)

## Description

The primary goal of this task is to create a Django-based REST-Api that manages
events (like conferences, meetups, etc.). The application will allow users to create,
view, update, and delete events. It should also handle user registrations for these
events.

## Key Requirements:

- [x] Design an Event model with fields such as title, description, date, location,
  and organizer.
- [x] Create custom user model for registration with email and
  password.
- [x] Implement CRUD (Create, Read, Update, Delete) operations for the Event
  model.
- [x] Basic User Registration and Authentication.
- [x] Event Registration.
- [x] Add unit tests.

### Bonus Points:

- [x] Containerize application with Docker, add Docker Compose.
- [x] Implement an advanced feature like event search or filtering.
- [x] Add a feature for sending email notifications to users upon event registration.

## Requirements

To run this API, you'll need:

- Python 3.11
- Django
- Django REST Framework
- Docker (optional)
- and other dependencies listed in the `requirements` folder

## Getting Started local

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ git clone https://github.com/MafanNam/python-drf-test-task.git

$ cd python-drf-test-task

$ virtualenv venv
$ source venv/bin/activate
$ # or windows
$ .\venv\Scripts\activate

$ pip install -r requirements/local.txt

$ cd backend/
$ python manage.py migrate
$ python manage.py loaddata mydata.json
$ python manage.py runserver
```

### If you want the api to send messages to mail

Then you MUST create and config `django.env` optional `django.docker.env`.

For example were create `django.example.env` optional `django.docker.example.env`

All these files are in [.envs/.local/](.envs/.local/)

You can now access the API in your browser at http://localhost:8000/.

## Getting Started with Docker

Commands can be run through a makefile or written manually.

You can now access the API in your browser at http://localhost:8000/. Flower http://localhost:5555/

### To build and raise a container, you just need to run it:

You cannot use makefile

```bash
$ docker compose -f local.yml up --build -d --remove-orphans
$ # or
$ docker compose -f local.yml up --build
```

You can use makefile

```bash
$ make build
$ # or
$ make build-log
```

### Basic commands:

```bash
$ make buld-log

$ make up

$ make down
```

## Run test

For testing and generate coverage

![cov tests](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/test_cov.png)

#### makefile

```bash
$ make cov
$ make cov-gen
```

#### no makefile

```bash
$ cd backend & coverage run --source='.' --omit='*/migrations/*.py,*/asgi.py,*/wsgi.py,*/manage.py' manage.py test
$ cd backend & coverage html
```

## API Documentation

The API documentation is not available [localhost:8000](http://localhost:8000).

![endpoint2](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/2.gif)
![endpoint3](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/3.gif)

### Admin

![admin](https://github.com/MafanNam/python-drf-test-task/blob/dev-0.0.1/screanshots/4.gif)

## Author

This project is developed by Mafan.

## License

This project is licensed under MIT License.
