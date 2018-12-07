import os
from services.Customer import Customer
from services.Order import Order

class LookupCustomerMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()
        self.__order = Order()

    def customerMenuSelection(self, customer):
            selection = ""
            os.system('cls')
            while (selection !="9"):
                print(customer)
                print("1. Update information ")
                print("2. Customer Order History")
                print("3. Remove Customer")
                print("9. Go Back")
                print("--------------")
                selection = input()
                os.system('cls')

                if selection == "1":
                    self.__manager.gotoclass("updateinformation", customer)

                elif selection == "2":
                    customer_ssn = customer[1]
                    user_history = self.__order.findUserHistory(customer_ssn)
                    for line in user_history:
                        print(line,end="\n")
                
                elif selection == "3":
                    ssn = customer[1]
                    self.__customer.deleteCustomer(customer, ssn)
                    customer = None
                    return customer