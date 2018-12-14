import os
from colorama import Fore

class ShowAllOrdersMenu:
    def __init__(self, manager):
        self.__manager = manager
    def showOrdersMenu(self):
        self.__manager.printHeader()
        show_order_menu_selection = ""
        while(show_order_menu_selection !="9"):
            Orders = self.__manager.getOrderManager().getOrders(True)
            for order in Orders:
                print(Fore.YELLOW,end="")
                print(order)
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            show_order_menu_selection = input()
            if show_order_menu_selection == "9":
                self.__manager.gotoClass("ordermenu")