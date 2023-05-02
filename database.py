from pymongo import MongoClient

mongo_client = MongoClient('mongo')
db = mongo_client['cse_312']
user_coll = db['chat']
