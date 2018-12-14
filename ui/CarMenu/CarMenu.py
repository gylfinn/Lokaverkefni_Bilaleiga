import os
from colorama import Fore

#This class is only 
class CarMenu:
    def __init__(self, manager):
        self.__manager = manager
    def carMenu(self):
        self.__manager.printHeader()
        car_menu_selection = ""
        while(car_menu_selection !="9"):
            print(Fore.GREEN,end="")
            if self.__manager.isAdmin():
                print("1. Car Administration")
                print("2. Fleet Manager")
                print("3. Car Order History")
            else:
                print("1. Fleet Manager")
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            car_menu_selection = input()
            if car_menu_selection == "1":
                if self.__manager.isAdmin():
                    self.__manager.gotoClass("caradministrationmenu")
                else:
                    self.__manager.gotoClass("fleetmenu")
            elif car_menu_selection == "2":
                if self.__manager.isAdmin():
                    self.__manager.gotoClass("fleetmenu")
                else:
                    pass #????
            elif car_menu_selection == "3":
                self.__manager.gotoClass("carhistory")
            elif car_menu_selection =="9":
                self.__manager.gotoClass("mainmenu")
