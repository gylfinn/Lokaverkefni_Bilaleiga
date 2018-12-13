import os
from colorama import Fore

class Overview:
    def __init__(self, manager):
        self.__manager = manager
    def overview(self):
        self.__manager.printHeader()
        menu_selection = ""
        while(menu_selection !="9"):
            self.__manager.getVehicleManager().loadVehicles()
            Vehicles = self.__manager.getVehicleManager().getVehicles()
            print(Fore.YELLOW,end="")
            for vehicle in Vehicles:
                print(vehicle)
            print(Fore.RED,end="")
            print("\n9. Back")
            print(Fore.WHITE,end="")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("fleetmenu")


                #Vehicles = self.__manager.getOrderManager().getOrders(True)