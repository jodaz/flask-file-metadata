from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/api/users', methods=['POST'])
def add_document():
    data = request.json
    new_user = mongo.db.users.insert_one(data)
    
    created_user = mongo.db.users.find_one({"_id": new_user.inserted_id})
    
    created_user["_id"] = str(created_user["_id"])
    
    return jsonify(created_user), 201

if __name__ == '__main__':
    app.run(debug=True)
