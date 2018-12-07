import os


class CurrentRentals:
    def __init__(self, manager):
        self.__manager = manager
    def currentRentals(self):
        os.system('cls')
        menu_selection = ""
        while(menu_selection !="9"):
            Vehicles = self.__manager.getVehicleManager().getRentedVehicles()
            for vehicle in Vehicles:
                print(vehicle)
            print("\n9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("fleetmenu")