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
            print("Car Menu")
            print(Fore.GREEN,end="")
            print("1. Car Administration")
            print("2. Fleet Manager")
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            car_menu_selection = input()
            os.system('cls')
            if car_menu_selection == "1":
                self.__manager.gotoClass("caradministrationmenu")
            elif car_menu_selection == "2":
                self.__manager.gotoClass("fleetmenu")
            elif car_menu_selection =="9":
                self.__manager.gotoClass("mainmenu")
