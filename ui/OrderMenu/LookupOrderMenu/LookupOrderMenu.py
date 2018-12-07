import os

#Þessi klasi þarf að kalla á klasa í services sem leitar að order
#og sýnir svo upplýsingar um þá order og býður notanda að velja 1,2,3
# fyrir cancel, change, chargeback
class LookupOrderMenu:
    def __init__(self, manager):
        self.__manager = manager

    def lookupOrderMenu(self):
        os.system('cls')
        lookup_order_selection = ""
        while(lookup_order_selection !="9"):
            print("Order info displayed here")
            print("1. Change order")
            print("2. Cancel Order")
            print("3. Chargeback Order")
            print("9. Back")
            lookup_order_selection = input()

            if lookup_order_selection == "1":
                self.__manager.gotoClass("")
            elif lookup_order_selection == "2":
                self.__manager.gotoClass("")
                #Calls cancel order service class
            elif lookup_order_selection == "3":    
                self.__manager.gotoClass("")
                #calls chargeback order service class
            elif lookup_order_selection == "9":
                self.__manager.gotoClass("lookupordermenu")