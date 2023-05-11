from pymongo import MongoClient

mongo_client = MongoClient('mongo')
db = mongo_client['cse_312']
users_coll = db['users_coll']
