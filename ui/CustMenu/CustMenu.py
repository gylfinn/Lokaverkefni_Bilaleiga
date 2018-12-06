import os

class CustMenu:
    def __init__():
        pass
    def customerMenu(self, check_if_admin):
        selection = ""
        os.system('cls')
        while (selection !="9"):
            print("Customers")
            print("1. Lookup Customer")
            if check_if_admin:
                print("2. Register Customer")
            print("9. Go Back")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                customer = self.__customer.lookUpCustomer()
                if customer != None:
                    Interface.customerMenuSelection(self, check_if_admin, customer)
                else:
                    print("Customer does not exist")                   
            elif selection == "2" and check_if_admin:
                self.__customer.registerCustomer()
                os.system('cls')