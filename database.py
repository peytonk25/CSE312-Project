from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://doadmin:50am2lqD7RkF3164@db-mongodb-nyc1-48915-f5ba4355.mongo.ondigitalocean.com/app_database?tls=true&authSource=admin&replicaSet=db-mongodb-nyc1-48915")
db = mongo_client['app_database']
users_coll = db['users_coll']