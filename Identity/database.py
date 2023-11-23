import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBClient:

    def __init__(self):
        uri = os.environ.get('MONGODB_URI')
        username = os.environ.get('MONGODB_USERNAME', '')
        password = os.environ.get('MONGODB_PASSWORD', '')

        if uri:
            uri = uri.replace('<username>', username).replace('<password>', password)

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.ping()

    """Check connection"""
    def ping(self):

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
