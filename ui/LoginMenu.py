from services.Login import Login
from services.servicehelpers.IsInfoValid import IsInfoValid
from ui.MainMenu import MainMenu
from colorama import Fore
import getpass
import os
import time

class LoginMenu:
    def __init__(self, mananger): 
        self.__login = Login()
        self.__getlogininfo = IsInfoValid()
        self.__manager = mananger
    def login_menu(self):
        os.system('cls') #  hreinsar console gluggann
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                self.isadmin = self.__login.isAdmin(username) #athugar hvort notandi sé með adminréttindi
                self.fullname = self.__getlogininfo.get_fullname
                self.__manager.gotoClass("mainmenu")
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print(Fore.RED,"Wrong Username and/or Password\n",Fore.WHITE)
    def header(self, check_if_admin, username):
        if check_if_admin:
            admintag = "(A)"
        else:
            admintag = ""
        print("------------------------------------")
        print("Welcome {}{} {}".format(username, admintag, time.ctime()))
        return