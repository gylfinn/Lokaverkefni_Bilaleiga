from repo.GetData import GetData
from services.servicehelpers.GetLoginInfo import IsInfoValid

class Login:
    def __init__(self): 
        self.__user_data = GetData('users.csv')
        self.__check_login_info = IsInfoValid()
        self.__raw_data = self.__user_data.readData()
    # Sendi usernameið og password í servicehelper til að athuga hvort það sé til
    def validUser(self, username, password):
        valid_user = self.__check_login_info.check_acc(self.__raw_data,username)
        valid_password = self.__check_login_info.check_pw(self.__raw_data, password)
        if valid_user:
            if valid_password:
                return True

    def isAdmin(self, username):
        is_admin = self.__check_login_info.check_admin(self.__raw_data, username)
        if is_admin:
            return True
    # kalla í 2 önnur föll "user exits" og "password match (correct password)"
    #def validateUser():
        