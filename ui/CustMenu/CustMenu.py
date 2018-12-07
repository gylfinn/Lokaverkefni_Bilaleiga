import os
from services.Customer import Customer

class CustMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def customerMenu(self):
        selection = ""
        os.system('cls')
        while (selection != "9"):
            print("Customers")
            print("1. Lookup Customer")
            print("2. Register Customer")
            print("9. Go Back")
            print("--------------")
            selection = input()
            os.system('cls')

            # kallar í annan UI klasa sem spyr um SSN og leita af viðskiptavininum

            if selection == "1":
                self.__manager.gotoClass("lookupcustomer")

            # kallar í anna UI klasa sem spyr um upplýsingar um notandann sem sendi þær áfram
            # í service og niður i repo sem skrifar gögnin    
            #               
            elif selection == "2":
                self.__manager.gotoClass("registercustomer")
