import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt_identity)
from flask_jwt_extended import jwt_required


app = Flask(__name__)
CORS(app)

# Configure the JWT manager
app.config['JWT_SECRET_KEY'] = 'mysecret-key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username = request.json.get('Username', None)
    password = request.json.get('Password', None)

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='userdb'
    )

    # Verify that the username and password are correct
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM userdetails WHERE Username=%s AND Password=%s', (username, password)
    )
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result is None:
        return jsonify({'msg': 'Wrong username or password'}), 401

    # Create the access token
    access_token = create_access_token(identity=username)

    return jsonify({'access_token': access_token})

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify({'logged_in_as': current_user}), 200

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5000)