import os
from colorama import Fore

#This class is only 
class CarAdministrationMenu:
    def __init__(self, manager):
        self.__manager = manager
    def carAdministrationMenu(self):
        os.system('cls')
        car_menu_selection = ""
        while(car_menu_selection !="9"):
            print("Car Administration Menu")
            print(Fore.GREEN,end="")
            print("1. Register new car")
            print("2. Deregister car")
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            car_menu_selection = input()
            os.system('cls')
            if car_menu_selection == "1":
                self.__manager.gotoClass("registernewcar")
            elif car_menu_selection == "2":
                self.__manager.gotoClass("deregistercar")
            elif car_menu_selection =="9":
                self.__manager.gotoClass("carmenu")