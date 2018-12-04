class IsInfoValid:
    def __init__(self):
        pass
    def check_acc(self,datalist, username):
        for line in datalist:
            if username == line[0]:
                return True
            
        return False
    
    def check_pw(self, datalist, password):
        for line in datalist:
            if password == line[4]:
                return True
        return False        

    def check_admin(self, datalist):
        for line in datalist:
            if line[5] == 1:
                return True
        return False




# username, name, address, phonenumber, password, admin
# admin, admin, menntavegur1, 5812345, admin, 1
# gylfi18, Gylfi Helgason, arnarhraun 36, 6931730, pass123, 0
#   0           1               2            3        4     5