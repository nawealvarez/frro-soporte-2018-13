from datos.usuarios import UserData
from werkzeug.security import check_password_hash, generate_password_hash

from entidades.objects import Usuario

class UserLogic():

    @staticmethod
    def insert_one(user):
        user.password = generate_password_hash(user.password)
        UserData.create_user(user)

    @staticmethod
    def find_by_username(username):
        user = UserData.find_by_username(username)
        return Usuario(user["username"], user["email"], user["_id"]) if user else None
        
    @staticmethod
    def check_password(password, username):
        pwhash = UserData.get_user_password(username)
        return check_password_hash(pwhash, password)


    @staticmethod 
    def find_by_id(userid):
        user = UserData.find_by_id(userid)
        return Usuario(user["username"], user["email"], user["_id"]) if user else None
