import pymongo

from datos.connection import Connection

class UserData():
    @staticmethod
    def create_user(user):
        db = Connection.connect()
        user._id = UserData.__generate_id()
        db.usuarios.insert_one(user.__dict__)

    @staticmethod
    def find_by_username(username):
        db = Connection.connect()
        return db.usuarios.find_one({"username": username})

    @staticmethod
    def find_by_prop(key, value):
        db = Connection.connect()
        return db.usuarios.find({key: value})
    
    @staticmethod
    def check_password(pwhash, username):
        db = Connection.connect()
        return True if db.usuarios.find_one({"username": username, "password": pwhash}) else False
   
    @staticmethod
    def find_by_id(userid):
        db = Connection.connect()
        return db.usuarios.find_one({"_id": userid})

    @staticmethod
    def __generate_id():
        db = Connection.connect()
        try:
            max_id = db.usuarios.find_one({}, {"_id": 1}, sort=[("_id", pymongo.DESCENDING)])["_id"]
        except:
            max_id = 0
        finally:
            return max_id + 1

    @staticmethod
    def get_user_password(username):
        return UserData.find_by_username(username)["password"]