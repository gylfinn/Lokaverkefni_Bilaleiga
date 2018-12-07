import os


class Overview:
    def __init__(self, manager):
        self.__manager = manager
    def overview(self):
        os.system('cls')
        menu_selection = ""
        while(menu_selection !="9"):
            Vehicles = self.__manager.getVehicleManager().getVehicles()
            for vehicle in Vehicles:
                print(vehicle)
            print("\n9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("ordermenu")


                #Vehicles = self.__manager.getOrderManager().getOrders(True)