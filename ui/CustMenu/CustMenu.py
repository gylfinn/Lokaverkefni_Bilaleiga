import os
from services.Customer import Customer

class CustMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def customerMenu(self):
        selection = ""
        os.system('cls')
        while (selection !="9"):
            print("Customers")
            print("1. Lookup Customer")
            print("2. Register Customer")
            print("9. Go Back")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                customer = self.__customer.lookUpCustomer()
                if customer != None:
                    self.__manager.gotoclass("lookupcustomermenu")
                    #LookupCustomerMenu(self, customer)
                else:
                    print("Customer does not exist")                   
            elif selection == "2":
                self.__customer.registerCustomer()
                os.system('cls')