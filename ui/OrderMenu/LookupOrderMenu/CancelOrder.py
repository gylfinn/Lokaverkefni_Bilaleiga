import os

# Þessi klasi spyr notandann hvort hann vilji confirma cancel order eða ekki
# ef hann velur YES þá er callað í service klasa sem eyðir orderinu
# ef nei, þá bara til baka

class CancelOrder:
    def __init__(self, manager):
        self._manager = manager
    def cancelOrder(self):
        os.system('cls')
        cancel_order_menu_selection = ""
        while(cancel_order_menu_selection !="9"):
            print("BACKEND FUNCTION MISSIN HERE")
            print("Are you sure you want to cancel %ORDER ID?%")
            print("1. Yes")
            print("2. No")
            print("9. Back")
            cancel_order_menu_selection = input()
            if cancel_order_menu_selection == "9":
                self._manager.gotoClass("lookupordermenu")
            elif cancel_order_menu_selection == "1":
                #call service class here
                pass
            elif cancel_order_menu_selection == "2":
                #call service class here
                pass