import os


class RegisterNewCar:
    def __init__(self, manager):
        self.__manager = manager
    def registerNewCar(self):
        os.system('cls')
        register_new_car_menu_selection = ""
        while(register_new_car_menu_selection !="9"):

            vehicle_reg_num = input("Registration number of new Vehicle: ")
            os.system('cls') #registrationnumber,rented,modelyear,brand,price,type
            print("Registration number of new Vehicle: {}".format(vehicle_reg_num))
            model_year = input("Model year of new Vehicle: ")
            os.system('cls')
            print("Registration number of new Vehicle: {}".format(vehicle_reg_num))
            print("Model year of new Vehicle: {}".format(model_year))
            vehicle_brand = input("Brand of Vehicle: ")
            os.system('cls')
            print("Registration number of new Vehicle: {}".format(vehicle_reg_num))
            print("Model year of new Vehicle: {}".format(model_year))
            print("Brand of Vehicle: {}".format(vehicle_brand))
            vehicle_type = input("Type of Vehicle (1 for Hatchback, 2 for Sedan, 3 for SUV): ")
            os.system('cls')
            print("Registration number of new Vehicle: {}".format(vehicle_reg_num))
            print("Model year of new Vehicle: {}".format(model_year))
            print("Brand of Vehicle: {}".format(vehicle_brand))
            print("Type of Vehicle (1 for Hatchback, 2 for Sedan, 3 for SUV): {}\n".format(vehicle_type))
            confirmation = input("Enter 8 to Confirm or 9 to Cancel")
            if confirmation == "8":
                vehicle_price = 0
                rented = False
                if vehicle_type == "1":
                    vehicle_price = 100
                elif vehicle_type == "2":
                    vehicle_price = 200
                elif vehicle_type == "3":
                    vehicle_price = 300
                self.__manager.getVehicleManager().registerNewVehicle(vehicle_reg_num, rented, model_year, vehicle_brand, vehicle_price, vehicle_type)

            if confirmation == "9":
                self.__manager.gotoClass("caradministrationmenu")