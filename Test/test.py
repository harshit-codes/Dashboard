from pymongo import MongoClient
import pymongo

from dotenv import load_dotenv
load_dotenv()
import os

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
CLUSTER = os.environ["CLUSTER"]

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://" + DB_USER + ":" + DB_PASS + "@" + CLUSTER + "/?retryWrites=true&w=majority"
print(CONNECTION_STRING)
print("mongodb+srv://harshit:K7W1QMAKsO4rJoT2@cluster0.mowez.mongodb.net/?retryWrites=true&w=majority")
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)

db = client["UserData"]
collection = db["Flask_mongo"]

collection.insert_one({"user_name":"1"})
collection.insert_one({"user_name":"2"})