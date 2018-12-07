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
            deregister_car_confirmation = input("Enter 8 to Confirm or 9 to Cancel")
            if deregister_car_confirmation == "8":
                deregister_car = self.__manager.getVehicleManager().deregisterVehicle(vehicle_reg_num)
                if deregister_car != None:
                    print("{} deregistered succesfully".format(vehicle_reg_num))
                else:
                    print("Could not find car with reg number: {}".format(vehicle_reg_num))
            elif deregister_car_confirmation == "9":
                self.__manager.gotoClass("caradministrationmenu")