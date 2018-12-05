from repo.GetData import GetData
from Models.Vehicle import Vehicle

REGISTRATION_NUMBER = 0
RENTED = 1
MODEL_YEAR = 2
BRAND = 3
PRICE = 4
CAR_TYPE = 5
class VehicleManger(object):
    def __init__(self):
        self.__Vehicles_Data = GetData("cars.csv").readData()
        self.__Vehicles = []
        self.__AvailableVehicles = []
        self.__VehiclesInRent = []
        self.loadVehicles()
        self.loadRentedVehicles()
        self.loadAvailableVehicles()
    def loadVehicles(self):
        for line in self.__Vehicles_Data:
            regnum = str(line).split(',')[REGISTRATION_NUMBER]
            rented = str(line).split(',')[RENTED]
            model_year = str(line).split(',')[MODEL_YEAR]
            brand = str(line).split(',')[BRAND]
            price = str(line).split(',')[PRICE]
            car_type = str(line).split(',')[CAR_TYPE]
            car = Vehicle(regnum, model_year, rented, brand, price, car_type)
            self.__Vehicles.append(car)
    def loadAvailableVehicles(self):
        for Veh in self.__Vehicles:
            if not Veh.getRented():
                self.__AvailableVehicles.append(Veh)
    def loadRentedVehicles(self):
        for Veh in self.__Vehicles:
            if Veh.getRented():
                self.__VehiclesInRent.append(Veh)
    def getVehicles(self):
        return self.__Vehicles
    def getAvailable(self):
        return self.__AvailableVehicles
    def getRentedVehicles(self):
        return self.__VehiclesInRent