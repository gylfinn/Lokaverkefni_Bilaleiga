import os


class DeregisterCar:
    def __init__(self, manager):
        self.__manager = manager
    def deregisterCar(self):
        os.system('cls')
        deregister_menu_selection = ""
        while(deregister_menu_selection !="9"):
            vehicle_reg_num = input("Registration number of Vehicle: ")
            os.system('cls') #registrationnumber,rented,modelyear,brand,price,type
            print("Registration number of Vehicle: {}".format(vehicle_reg_num))
            confirm = input("Enter 8 to Confirm or 9 to Cancel")
            #klara
            if confirm == "9":
                self.__manager.gotoClass("caradministrationmenu")