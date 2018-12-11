import os
from services.Customer import Customer
from colorama import Fore

NAME = 0
SSN = 1
ADDRESS = 2
PHONENUM = 3
DRIVERLICENCENUM = 4

class LookUpCustomerMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def customerMenuSelection(self):
            selection = ""
            SSN_input = input("Customer SSN:")
            customer = self.__customer.lookUpCustomer(SSN_input)
            self.__manager.setMetadata(customer)
            
            os.system('cls')
            while (selection != "9") and customer != None:
                print(Fore.YELLOW,end="")
                print("Name: {} ".format(customer[NAME]))
                print("SSN: {} ".format(customer[SSN]))
                print("Adress: {} ".format(customer[ADDRESS]))
                print("Phone Number: {} ".format(customer[PHONENUM]))
                print("Driver Licence Number {}".format(customer[DRIVERLICENCENUM])) 
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
                    self.__manager.gotoClass("updateinformation")9
                elif selection == "2":
                    user_history = self.__manager.getOrderManager().getOrdersByCustomer(SSN_input)
                    for order in user_history:
                        print(order, end="\n")
                elif selection == "3":
                    self.__customer.deleteCustomer(customer, SSN_input)
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