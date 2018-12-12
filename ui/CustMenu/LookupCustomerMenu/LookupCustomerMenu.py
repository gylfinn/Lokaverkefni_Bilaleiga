import os
from services.CustomerManager import CustomerManager
from colorama import Fore

NAME = 0
SSN = 1
ADDRESS = 2
PHONENUM = 3
DRIVERLICENCENUM = 4

class LookUpCustomerMenu:
    def __init__(self, manager):
        self.__manager = manager
    def customerMenuSelection(self):
            selection = ""
            SSN_input = input("Customer SSN: ")
            customer = self.__manager.getCustomerManager().findCustomer(SSN_input)
            self.__manager.setMetadata(customer)
            os.system('cls')
            while (selection != "9") and customer != None:
                print(Fore.YELLOW,end="")
                print("Name: {} ".format(customer.getName()))
                print("SSN: {} ".format(customer.getSSN()))
                print("Address: {} ".format(customer.getAddress()))
                print("Phone Number: {} ".format(customer.getPhoneNumber()))
                print("Driver Licence Number {}".format(customer.getDriversLicenseNumber())) 
                print(Fore.GREEN,end="")
                print("1. Update information ")
                print("2. Customer Order History")
                print("3. Remove Customer")
                print(Fore.RED,end="")
                print("9. Go Back")
                print(Fore.WHITE,end="")
                print("--------------")
                selection = input()
                os.system('cls')

                if selection == "1":
                    self.__manager.gotoClass("updateinformation")
                elif selection == "2":
                    self.__manager.gotoClass("lookupcustomerhistory")
                elif selection == "3":
                    self.__manager.getCustomerManager().removeCustomer(customer)
                    self.__manager.clearMetadata()
                elif selection == "9":
                    self.__manager.gotoClass("custmenu")
                    self.__manager.clearMetadata()

            if customer == None:
                print(Fore.RED,end="")
                print("Customer Does Not Exist! ")
                print(Fore.GREEN,end="")
                print("1. Search Again")
                print(Fore.RED,end="")
                print("9. Go Back")
                print(Fore.WHITE,end="")
                action = input()
                os.system('cls')
                if action == "1":
                    self.__manager.gotoClass("lookupcustomermenu")
                else:
                    self.__manager.gotoClass("custmenu")