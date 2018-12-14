import os
from colorama import Fore

#This class calls a service class that returns this class a list of upcoming orders
#This class then displays that to the user
#Action should be to select one of the orders and to go back
class UpcomingOrders:
    def __init__(self, manager):
        self.__manager = manager

    def upcomingOrders(self):
        self.__manager.printHeader()
        upcoming_order_menu_selection = ""
        while(upcoming_order_menu_selection !="9"):
            Orders = self.__manager.getOrderManager().getUpCommingOrders()
            for order in Orders:
                print(Fore.YELLOW,end="")
                print(order)
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("ordermenu")
