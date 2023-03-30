from flask import Flask, jsonify, request
from bson import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['usersdb']
users_collection = db['users']

# Returns a list of all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

# Returns the user with the specified ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'})

# Creates a new user with the specified data
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    result = users_collection.insert_one(user_data)
    return jsonify({'message': 'User created successfully', 'id': str(result.inserted_id)})

# Updates the user with the specified ID with the new data
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': user_data})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

# Deletes the user with the specified ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
