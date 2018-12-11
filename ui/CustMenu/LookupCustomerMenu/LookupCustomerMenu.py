import os
from services.Customer import Customer

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
            while (selection != "9"):
                print(customer)
                print("1. Update information ")
                print("2. Customer Order History")
                print("3. Remove Customer")
                print("9. Go Back")
                print("--------------")
                selection = input()
                os.system('cls')

                if selection == "1":
                    self.__manager.gotoClass("updateinformation", customer)
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