from services.Login import Login
import getpass
import os
import time

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
                Interface.mainMenu(self, check_if_admin, username)
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print("Wrong Username and/or Password\n")

    def header(self, check_if_admin, username,):
        if check_if_admin:
            admintag = "(A)"
        else:
            admintag = ""
        print("------------------------------------")
        print("Welcome {}{} {}".format(username, admintag, time.ctime()))
        return

    def mainMenu(self, check_if_admin, username):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            Interface.header(self, check_if_admin, username)
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
        order_selection = ""
        while(order_selection !="9"):
            print("Order Menu")
            print("1. Upcoming Orders")
            print("2. New Orders")
            print("3. Lookup Orders")
            print("8. Back")
            print("9. Main Menu")
            print("--------------")
            order_selection = input()
            os.system('cls')

            if order_selection == "1":
                #Interface.upcomingOrderMenu(self)
                pass
            elif order_selection == "2":
                #Interface.newOrderMenu(self)
                pass
            elif order_selection == "3":
                #Interface.LookupOrderMenu(self)
                pass
            elif order_selection == "8":
                #Interface.CarMenu(self)
                pass
            elif order_selection == "9":
                #Interface.loginScreen(self)
                pass

    def upcomingOrderMenu(self):
        os.system('cls')
        upcomingOrderMenu_selection = ""
        while(upcomingOrderMenu_selection !="9"):
            print("Upcoming Orders:")
            print("1. Upcoming Orders")
            print("2. New Orders")
            print("3. Lookup Orders")
            print("8. Back")
            print("9. Main Menu")
            print("--------------")
            upcomingOrderMenu_selection = input()
            os.system('cls')        #Hér kermur listi af orders



    def carMenu(self, check_if_admin):
        os.system('cls')
        car_selection = ""
        while(car_selection !="9"):
            print("Cars")
            print("1. Total fleet")
            if check_if_admin:
                print("2. Car Administration")
            print("9. Main Menu")
            print("--------------")
            car_selection = input()
            os.system('cls')

    def customerMenu(self, check_if_admin):
        selection = ""
        os.system('cls')
        while (selection !="9"):
            print("Customers")
            print("1. Lookup Customer")
            if check_if_admin:
                print("2. Register Customer")
            print("9. Go Back")
            selection = input()
            os.system('cls')

            if selection == "1":
                customer = self.__customer.lookUpCustomer()
                print(customer)
            if selection == "2" and check_if_admin:
                self.__customer.registerCustomer()

