from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://doapps-1ed21c95-ed6b-4356-ad32-6f090b16b2f4:2kh0K5B4SU3Qq761@db-mongodb-nyc1-48915-f5ba4355.mongo.ondigitalocean.com/app_database?tls=true&authSource=admin&replicaSet=db-mongodb-nyc1-48915")
db = mongo_client['app_database']
users_coll = db['users_coll']