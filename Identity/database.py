import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Core.settings import Settings
from Core.models import ResponseModel

from Identity.models import Users


class MongoDBClient:

    def __init__(self):
        setting = Settings.get_settings()
        uri = setting.MONGODB_URI
        username = setting.MONGODB_USERNAME
        password = setting.MONGODB_PASSWORD

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
            print("Pinged, You successfully connected to database")
        except Exception as e:
            print(e)

    """validate user credendials"""
    def validate_user(self, username: str, password:str) -> dict:
        response = ResponseModel(status=False, message="", data=None)
        try:
            # add logic to validate user
            user = self.client.Identity.Users.find_one({'username': username})
            if user is None:
                response.message = f'User is not resigtered please signup.'
                return response
            
            user = Users(**user)
            decrypt_password = user.password
            if decrypt_password != password:
                response.message = f'Incorrect password please provide valid password.'
                return response

            response.status = True
            response.message = 'User validated successfully.'
            response.data = json.dumps(user)
        except Exception as e:
            response.message = str(e)
        
        return response
