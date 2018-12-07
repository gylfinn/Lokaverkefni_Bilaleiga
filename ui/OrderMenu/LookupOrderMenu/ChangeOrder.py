import os

# Þessi klasi biður notanda að slá inn nýtt info um order
# ef hann confirmar þá er kallað í service class sem skrifað nýja info í CSV
# ef hann gerir back þá fer hann back duh

class ChangeOrder:
    def __init__(self, manager):
        self._manager = manager
    def changeOrder(self):
        os.system('cls')
        change_order_menu_selection = ""
        while(change_order_menu_selection !="9"):
            print("BACKEND FUNCTION MISSIN HERE")
            print("Changing order %ORDER ID?%")
            print("Name: ")
            print("Date: ")
            print("Car: ")
            print("1. Confirm")
            print("9. Back")
            change_order_menu_selection = input()
            if change_order_menu_selection == "9":
                self._manager.gotoClass("lookupordermenu")
            elif change_order_menu_selection == "1":
                #call service class here
                pass