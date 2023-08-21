
from pymongo import MongoClient
import os 
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('uri')
# Connect to the MongoDB database

client = MongoClient(uri)
db = client.hi
collection = db.by 
collection.insert_one({'name': 'kuleep'})