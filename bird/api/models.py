from pymongo import MongoClient
from django.conf import settings


def get_connection(collection, database=None):
	db_collection = None
	try:
		client = MongoClient(connect=True)
		db = client[database if database else settings.DATABASE]
		db_collection = db[collection]
		
	except Exception, e:
		print "Failed to establish MongoDB connection"

	return db_collection