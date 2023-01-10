from flask import Flask, request, jsonify
import datetime
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_cors import CORS
from flask_cors import CORS, cross_origin
  
app = Flask(__name__)
CORS(app)
x = datetime.datetime.now()
app.config["JWT_SECRET_KEY"] = "mySecretkey"
jwt = JWTManager(app)
  
# Initializing flask app

  
@app.route('/login', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test@g.in" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body
# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"Samina", 
        "Email":"samina.mulla@tdtl.world",
        "Date":x, 
        "programming":"python"
        }
  
      
# Running app
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5000)