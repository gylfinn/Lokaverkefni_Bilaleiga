from services.Login import Login
import getpass
import os
import time

class LoginMenu:
    def __init__(self): 
        self.__login = Login()

    def header(self, check_if_admin, username):
        if check_if_admin:
            admintag = "(A)"
        else:
            admintag = ""
        print("------------------------------------")
        print("Welcome {}{} {}".format(username, admintag, time.ctime()))
        return

    def loginScreen(self):
        os.system('cls') #  hreinsar console gluggann
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                check_if_admin = self.__login.isAdmin(username) #athugar hvort notandi sé með adminréttindi
                MainMenu.mainMenu(self, check_if_admin, username)
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print("Wrong Username and/or Password\n")