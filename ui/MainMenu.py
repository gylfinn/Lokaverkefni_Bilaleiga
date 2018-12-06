import os

class MainMenu:
    def __init__(self, manager):
        self.__manager = manager
    def main_menu(self):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            print("Main Menu")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print("9. Log out")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                self.__manager.gotoClass("ordermenu")
            elif selection == "2":
                self.__manager.gotoClass("carmenu")
            elif selection == "3":
                self.__manager.gotoClass("customermenu")
            elif selection == "9":
                self.__manager.gotoClass("loginmenu")