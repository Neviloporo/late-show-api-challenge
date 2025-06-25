
# Late Show API Challenge

A RESTful API built with Flask to manage a Late Night TV show system, featuring token-based authentication and PostgreSQL integration.

## Folder Structure

This is the folder structure of the late-show-api

late-show-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── .gitignore
├── Pipfile
├── Pipfile.lock
└── README.md




## Setup Instructions

###  Dependencies

Install with Pipenv:

pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary

pipenv shell


###  PostgreSQL Database

Create the database:
CREATE DATABASE late_show_db;


## Set your DATABASE_URL in `server/config.py`:


SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"


### Migrations and Seed

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py


##  Authentication Flow

- **POST /register** — Create a new user
- **POST /login** — Returns a JWT access token

Protected endpoints:

- `POST /users`
- `POST /tokens`
- `DELETE /episodes`
- `GET /episodes`



##  API Endpoints

| Method | Route                         | Auth Required | Description                         |
|--------|-------------------------------|---------------- |-----------------------------------|
| POST   | `/register`                  | ❌              | Register a new user                |
| POST   | `/login`                     | ❌              | Log in and receive JWT             |
| GET    | `/episodes`                  | ❌              | List all episodes                  |
| GET    | `/episodes/<id>`             | ❌              | View specific episode + guests     |
| DELETE | `/episodes/<id>`             | ✅              | Delete episode + appearances       |
| GET    | `/guests`                    | ❌              | List all guests                    |
| POST   | `/appearances`               | ✅              | Create a new guest appearance      |



##  Postman Testing Guide

1. Import `challenge-4-lateshow.postman_collection.json` into Postman.
2. Run these flows:

   - Register a user
   - Log in to receive a JWT token
   - Use the token in protected requests



## Sample Screenshots

### POST /users

![GET Episodes](./Screenshots/Screenshot%20from%202025-06-24%2012-21-10.png)

### POST /tokens

![POST Appearance](./Screenshots/Screenshot%20from%202025-06-24%2012-21-28.png)

### DELETE /episodes

![DELETE Episode](./Screenshots/Screenshot%20from%202025-06-25%2009-12-07.png)

### GET /episodes

![GET Episodes](./Screenshots/Screenshot%20from%202025-06-25%2009-12-38.png)





