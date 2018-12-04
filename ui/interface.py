from services.login import Login
import getpass
import os

class Interface:
    def __init__(self): 
        self.__login = Login()

    def login_screen(self):
        os.system('cls') #  hreinsar console gluggann
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                check_if_admin = self.__login.isAdmin() #athugar hvort notandi sé með adminréttindi
                Interface.main_menu(self, check_if_admin)
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print("Wrong Username and/or Password\n")


    def main_menu(self, is_admin):
        os.system('cls')
        action = ""
        while(action !="9"):
            print("Main Menu")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print("9. Log out")
            print("--------------")
            action = input()
            os.system('cls')