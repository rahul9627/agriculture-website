from flask_login import UserMixin
from pymongo import MongoClient
import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

# Initialize Bcrypt
bcrypt = Bcrypt()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "agriculture_website"
COLLECTION_NAME = "users"

# Global client
_mongo_client = None

def get_mongo_client():
    global _mongo_client
    if _mongo_client is None and MONGO_URI:
        try:
            _mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        except Exception as e:
            print(f"MongoDB connection setup failed: {e}")
    return _mongo_client

def get_users_collection():
    client = get_mongo_client()
    if client:
        return client[DB_NAME][COLLECTION_NAME]
    return None

class User(UserMixin):
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self.id = str(_id) if _id else None

    @staticmethod
    def get(user_id):
        collection = get_users_collection()
        if collection is not None:
            try:
                from bson.objectid import ObjectId
                user_data = collection.find_one({"_id": ObjectId(user_id)})
                if user_data:
                    return User(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        _id=user_data['_id']
                    )
            except Exception:
                pass
        return None

    @staticmethod
    def find_by_email(email):
        collection = get_users_collection()
        if collection is not None:
            user_data = collection.find_one({"email": email})
            if user_data:
                return User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password'],
                    _id=user_data['_id']
                )
        return None
    
    @staticmethod
    def find_by_username(username):
        collection = get_users_collection()
        if collection is not None:
            user_data = collection.find_one({"username": username})
            if user_data:
                return User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password'],
                    _id=user_data['_id']
                )
        return None

    def save(self):
        collection = get_users_collection()
        if collection is not None:
            try:
                user_data = {
                    "username": self.username,
                    "email": self.email,
                    "password": self.password
                }
                result = collection.insert_one(user_data)
                self.id = str(result.inserted_id)
                return True
            except Exception as e:
                print(f"Error saving user to MongoDB: {e}")
                return False
        else:
            print("Error: User collection not available - MongoDB connection failed or not configured.")
        return False
