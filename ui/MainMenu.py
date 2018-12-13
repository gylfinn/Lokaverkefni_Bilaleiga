import os
from colorama import Fore
# from ui.Header import Header

class MainMenu:
    def __init__(self, manager):
        self.__manager = manager
    def main_menu(self):
        self.__manager.printHeader()
        selection = ""
        while(selection !="9"):
            print(Fore.GREEN,end="")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print(Fore.RED,end="")
            print("9. Log out")
            print(Fore.WHITE,end="")
            selection = input()
            os.system('cls')

            if selection == "1":
                self.__manager.gotoClass("ordermenu")
            elif selection == "2":
                self.__manager.gotoClass("carmenu")
            elif selection == "3":
                self.__manager.gotoClass("custmenu")
            elif selection == "9":
                self.__manager.gotoClass("loginmenu")