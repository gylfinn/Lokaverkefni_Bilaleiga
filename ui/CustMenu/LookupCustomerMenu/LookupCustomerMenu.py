import os
from services.Customer import Customer
from colorama import Fore

NAME = 0
SSN = 1
ADRESS = 2
PHONENUM = 3
DRIVERLICENCENUM = 4

class LookUpCustomerMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def customerMenuSelection(self):
            selection = ""
            SSN = input("Customer SSN:")
            customer = self.__customer.lookUpCustomer(SSN)
            self.__manager.setMetadata(customer)
            
            os.system('cls')
            while (selection != "9") and customer != None:
                print(Fore.YELLOW,end="")
                print("Name: {} ".format(customer[0]))
                print("SSN: {} ".format(customer[1]))
                print("Adress: {} ".format(customer[2]))
                print("Phone Number: {} ".format(customer[3]))
                print("Driver Licence Number {}".format(customer[4])) 
                print(Fore.WHITE)
                print("1. Update information ")
                print("2. Customer Order History")
                print("3. Remove Customer")
                print("9. Go Back")
                print("--------------")
                selection = input()
                os.system('cls')

                if selection == "1":
                    self.__manager.setMetadata(customer)
                    self.__manager.gotoClass("updateinformation")
                elif selection == "2":
                    user_history = self.__manager.getOrderManager().getOrdersByCustomer(SSN)
                    for order in user_history:
                        print(order, end="\n")
                elif selection == "3":
                    self.__customer.deleteCustomer(customer, SSN)
                    customer = None
                    return customer
                elif selection == "9":
                    self.__manager.gotoClass("custmenu")
                    self.__manager.clearMetadata()

            if customer == None:
                print("Customer Does Not Exist! ")
                print("1. Search Again")
                print("9. Go Back")
                action = input()
                os.system('cls')
                if action == "1":
                    self.__manager.gotoClass("lookupcustomermenu")
                else:
                    self.__manager.gotoClass("custmenu")