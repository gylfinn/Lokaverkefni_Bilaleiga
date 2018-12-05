USERNAME = 0
PASSWORD = 4
ADMIN = 5
FULLNAME = 1

class IsInfoValid:
    def __init__(self):
        pass
    def check_acc(self,datalist, username):
        for line in datalist:
            if username == line[USERNAME]:
                return True 
            
        return False
    
    def check_pw(self, datalist, password):
        for line in datalist:
            if password == line[PASSWORD]:
                return True
        return False        

    def check_admin(self, datalist, username):
        for line in datalist:
            if username == line[USERNAME]:
                if '1' == line[ADMIN]:
                    return True
                return False

    def get_fullname(self, datalist, username):
        for line in datalist:
            if username in line:
                return line[FULLNAME]




# username, name, address, phonenumber, password, admin
# admin, admin, menntavegur1, 5812345, admin, 1
# gylfi18, Gylfi Helgason, arnarhraun 36, 6931730, pass123, 0
#   0           1               2            3        4     5
