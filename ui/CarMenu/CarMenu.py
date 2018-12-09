import os

#This class is only 
class CarMenu:
    def __init__(self, manager):
        self.__manager = manager
    def carMenu(self):
        os.system('cls')
        car_menu_selection = ""
        while(car_menu_selection !="9"):
            print("Car Menu")
            print("1. Car Administration")
            print("2. Fleet Manager")
            print("9. Back")
            car_menu_selection = input()
            os.system('cls')
            if car_menu_selection == "1":
                self.__manager.gotoClass("caradministration")
            elif car_menu_selection == "2":
                self.__manager.gotoClass("fleetmenu")
            elif car_menu_selection =="9":
                self.__manager.gotoClass("mainmenu")
                