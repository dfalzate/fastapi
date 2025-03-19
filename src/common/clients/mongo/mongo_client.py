from pymongo import MongoClient
from  config.config import MONGO_URI, MONGO_DB_NAME 

db_client = MongoClient(MONGO_URI)
db = db_client[MONGO_DB_NAME]