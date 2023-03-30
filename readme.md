Flask Application for CRUD operations on MongoDB
This is a simple Flask application that provides REST API endpoints for CRUD operations on a User resource using MongoDB as the backend database.

Requirements
-Python 3
-Flask
-PyMongo

Installation
Clone the repository: git clone https://github.com/example/flask-mongo-crud.git
Install the required packages: pip install -r requirements.txt
Usage
Start the Flask application: python app.py
Use the following endpoints to interact with the User resource:
GET /users - Returns a list of all users.
GET /users/<id> - Returns the user with the specified ID.
POST /users - Creates a new user with the specified data.
PUT /users/<id> - Updates the user with the specified ID with the new data.
DELETE /users/<id> - Deletes the user with the specified ID.
