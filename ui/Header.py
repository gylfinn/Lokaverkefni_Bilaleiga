import time
import os

class Header:
    def __init__(self):
        self.__nextmenu = None
        self.__tree_list = []
        self.__isadmin = False
        self.__fullname = ""
    
    def printHeader(self):
        if self.__isadmin:
            admintag = "(A)"
        else:
            admintag = ""

        os.system('cls')
        print('-' * 75)
        print("Welcome {}{}{}{}".format(str(self.__fullname), admintag,"CAR RENTAL".rjust(10), time.ctime().rjust(10)))
        print('-' * 75)
        return

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