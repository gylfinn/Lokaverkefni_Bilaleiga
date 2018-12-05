from services.login import Login
import getpass
import os

class Interface:
    def __init__(self): 
        self.__login = Login()

    def loginScreen(self):
        os.system('cls') #  hreinsar console gluggann
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                check_if_admin = self.__login.isAdmin(username) #athugar hvort notandi sé með adminréttindi
                Interface.mainMenu(self, check_if_admin)
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print("Wrong Username and/or Password\n")


    def mainMenu(self, check_if_admin):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            print("Main Menu")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print("9. Log out")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                Interface.orderMenu(self)
            elif selection == "2":
                Interface.carMenu(self, check_if_admin)
            elif selection == "3":
                Interface.customerMenu(self, check_if_admin)
            elif selection == "9":
                Interface.loginScreen(self)

    def orderMenu(self):
        os.system('cls')
        action = ""
        while(action !="9"):
            print("Order Menu")
            print("1. Upcoming Orders")
            print("2. New Orders")
            print("3. Lookup Orders")
            print("9. Main Menu")
            print("--------------")
            action = input()
            os.system('cls')

    def carMenu(self, check_if_admin):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            print("Cars")
            print("1. Total fleet")
            if check_if_admin:
                print("2. Car Administration")
            print("9. Main Menu")
            print("--------------")
            selection = input()
            os.system('cls')

    def customerMenu(self, check_if_admin):
        os.system('cls')
        selection = ""
        while (selection !="9"):
            print("Customers")
            print("1. Lookup Customer")
            if check_if_admin:
                print("2. Register Customer")
            print("9. Go Back")
