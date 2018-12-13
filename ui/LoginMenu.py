from services.Login import Login
from services.servicehelpers.IsInfoValid import IsInfoValid
from ui.MainMenu import MainMenu
from ui.Header import Header
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
        self.__manager.printLoginHeader()
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                self.isadmin = self.__login.isAdmin(username) #athugar hvort notandi sé með adminréttindi
                self.fullname = self.__login.getFullname(username)
                self.__manager.setHeader()
                self.__manager.gotoClass("mainmenu")
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print(Fore.RED,"Wrong Username and/or Password\n",Fore.WHITE)