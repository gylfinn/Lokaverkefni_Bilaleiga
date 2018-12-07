import os

# Þessi klasi spyr notanda hvort hann vilji chargebacka order
# ef hann confirmar þá er kallað í service class
# ef hann gerir back þá fer hann back duh

class ChargebackOrder:
    def __init__(self, manager):
        self._manager = manager
    def chargebackOrder(self):
        os.system('cls')
        chargeback_order_menu_selection = ""
        while(chargeback_order_menu_selection !="9"):
            print("BACKEND FUNCTION MISSIN HERE")
            print("Chargeback order %ORDER ID?%")
            print("Name: ")
            print("Date: ")
            print("Car: ")
            print("1. Confirm chargeback?")
            print("9. Back")
            chargeback_order_menu_selection = input()
            if chargeback_order_menu_selection == "9":
                self._manager.gotoClass("lookupordermenu")
            elif chargeback_order_menu_selection == "1":
                #call service class here
                pass