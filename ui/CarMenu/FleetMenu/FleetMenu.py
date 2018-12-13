import os
from colorama import Fore

#This class is only 
class FleetMenu:
    def __init__(self, manager):
        self.__manager = manager
    def fleetMenu(self):
        os.system('cls')
        fleet_menu_selection = ""
        while(fleet_menu_selection !="9"):
            print("Fleet Menu")
            print(Fore.GREEN,end="")
            print("1. Overview")
            print("2. Current Rentals")
            print("3. Available")
            print("4. Return Car")
            print("5. Rent Car")
            print(Fore.RED,end="")
            print("9. Go Back")
            print(Fore.WHITE,end="")
            fleet_menu_selection = input()
            os.system('cls')
            if fleet_menu_selection == "1":
                self.__manager.gotoClass("overview")
            elif fleet_menu_selection == "2":
                self.__manager.gotoClass("currentrentals")
            elif fleet_menu_selection == "3":
                self.__manager.gotoClass("available")
            elif fleet_menu_selection == "4":
                self.__manager.gotoClass("returncar")
            elif fleet_menu_selection == "5":
                self.__manager.gotoClass("rentcar")
            elif fleet_menu_selection == "9":
                self.__manager.gotoClass("carmenu")