import os
from colorama import Fore

class VehicleHistoryMenu:
    def __init__(self, manager):
        self.__manager = manager
    def showVehicleHistory(self):
        self.__manager.printHeader()
        show_history_menu_selection = ""
        while(show_history_menu_selection !="9"):
            reg_number = input("Car Registration Number:")
            vehicle_history = self.__manager.getOrderManager().getOrdersByVehicle(reg_number)
            print("Found {} order(s) that had the registration number '{}'".format(len(vehicle_history), reg_number))
            for order in vehicle_history:
                print(Fore.YELLOW,end="")
                print(order)
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            show_history_menu_selection = input()
            if show_history_menu_selection == "9":
                self.__manager.gotoClass("carmenu")