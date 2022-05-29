from pymongo import MongoClient
import pymongo, pandas as pd

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

databaseList = client.list_database_names()
databseFocus = 'Dashboard'

db = client[databseFocus]
collectionList = db.list_collection_names()

print()