import time
import os

class Header:
    def __init__(self):
        self.__nextmenu = None
        self.__tree_list = []
        self.__isadmin = False
        self.__fullname = ""
    

    def printLoginHeader(self):
        os.system('cls')
        print('-' * 75)
        print("{}{}".format("PLEASE LOG IN TO CONTINUE".ljust(30), time.ctime().rjust(30)))
        print('-' * 75)

    def printHeader(self, location):

        location = "mAINMENU"

        if self.__isadmin:
            admintag = "(A)"
        else:
            admintag = ""

        displayname = self.__fullname + admintag

        #location = self.GetLocation(location)

        os.system('cls')
        print('-' * 75)
        print("Welcome {}{}".format(displayname.ljust(30), time.ctime().rjust(30)))
        print('-' * 75)
        print(location)

    def setIsAdmin(self, isadmin):
        if isadmin:
            self.__isadmin = True
        else:
            self.__isadmin = False

    def setFullname(self, fullname):
        self.__fullname = fullname

    def getNextMenu(self):
        return self.__nextmenu
    
    def setNextMenu(self, nextmenu):
        self.__nextmenu = nextmenu
        self.__tree_list.append(self.__nextmenu)
        
    def clearNextMenu(self):
        self.__nextmenu = None