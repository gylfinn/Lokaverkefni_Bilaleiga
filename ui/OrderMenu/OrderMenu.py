import os
from colorama import Fore

#This class is only 
class OrderMenu:
    def __init__(self, manager):
        self.__manager = manager

    def orderMenu(self):
        self.__manager.printHeader()
        order_menu_selection = ""
        while(order_menu_selection !="9"):
            print("Order Menu")
            print(Fore.GREEN,end="")
            print("1. Upcoming Orders")
            print("2. Show All Orders")
            print("3. New Order")
            print("4. Look Up Order")
            print("5. Price Calculator")
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            order_menu_selection = input()
            if order_menu_selection == "1":
                self.__manager.gotoClass("upcomingorders")
            elif order_menu_selection == "2":
                self.__manager.gotoClass("showallorders")
            elif order_menu_selection == "3":
                self.__manager.gotoClass("neworder")
            elif order_menu_selection == "4":
                self.__manager.gotoClass("lookupordermenu")
            elif order_menu_selection == "5":
                self.__manager.gotoClass("pricecalculator")
            elif order_menu_selection =="9":
                self.__manager.gotoClass("mainmenu")