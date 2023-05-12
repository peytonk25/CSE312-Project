from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://doapps-1ed21c95-ed6b-4356-ad32-6f090b16b2f4:39bz4C70DLw6e12g@db-mongodb-nyc1-48915-f5ba4355.mongo.ondigitalocean.com/admin?authSource=admin&tls=true")
db = mongo_client['app_database']
users_coll = db['users_coll']