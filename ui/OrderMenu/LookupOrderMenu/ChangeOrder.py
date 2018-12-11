import os
from colorama import Fore
from Models.Order import Order

# Þessi klasi biður notanda að slá inn nýtt info um order
# ef hann confirmar þá er kallað í service class sem skrifað nýja info í CSV
# ef hann gerir back þá fer hann back duh

class ChangeOrder:
    def __init__(self, manager):
        self.__manager = manager
    def changeOrder(self):
        os.system('cls')
        change_order_menu_selection = ""
        order = self.__manager.getMetadata()
        while(change_order_menu_selection !="9"):
            print("Changing order ", order.getOrderid())
            print(Fore.RED, "***Leaving field empty will keep the default the value***", Fore.WHITE)
            print("Changing SSN")
            order.setCustomerSSN(input() or order.getCustomerSSN())
            print("Change Date from:")
            order.setDateFrom(input() or order.getDateFrom())
            print("Change Date to:")
            order.setDateTo(input() or order.getDateTo())
            print("Car Registration Number:")
            order.setCarRegistration(input() or order.getCarRegistration())
            print(order)
            print(Fore.GREEN, "1. Confirm", Fore.WHITE)
            print(Fore.RED, "9. Back", Fore.WHITE)
            change_order_menu_selection = input()
            if change_order_menu_selection == "9":
                self.__manager.gotoClass("lookupordermenu")
            elif change_order_menu_selection == "1":
                self.__manager.gotoClass("lookupordermenu")