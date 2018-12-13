import os
from colorama import Fore
from Models.Vehicle import Vehicle

class ReturnCar:
    def __init__(self, manager):
        self.__manager = manager
    def returnCar(self):
        self.__manager.printHeader()
        menu_selection = ""
        while(menu_selection !="9"):
            Vehicles = self.__manager.getVehicleManager().getRentedVehicles()
            print(Fore.YELLOW,end="")
            for vehicle in Vehicles:
                print(vehicle)
            regnum = input("Enter Registration Number of the Vehicle: ")
            change_rented_status = self.__manager.getVehicleManager().changeVehicleStatus(regnum)
            if change_rented_status:
                print("Successfully changed the rented status of {}.".format(regnum))
            else:
                print("Could not change the rented status of {}.".format(regnum))
            print(Fore.RED,end="")
            print("\n9. Back")
            print(Fore.WHITE,end="")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("fleetmenu")