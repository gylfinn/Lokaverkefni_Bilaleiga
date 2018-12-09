from repo.GetData import GetData
from repo.SaveData import SaveData
from Models.Vehicle import Vehicle

REGISTRATION_NUMBER = 0
RENTED = 1
MODEL_YEAR = 2
BRAND = 3
PRICE = 4
CAR_TYPE = 5
VEHICLE_FILE = "cars.csv"
class VehicleManager(object):
    def __init__(self):

        self.__Vehicles_Data = GetData(VEHICLE_FILE).readData()
        self.__Vehicles = []
        self.__AvailableVehicles = []
        self.__VehiclesInRent = []
        self.__DataSaver = SaveData(VEHICLE_FILE)
        self.loadVehicles()
        self.loadRentedVehicles()
        self.loadAvailableVehicles()

    def loadVehicles(self):
        for line in self.__Vehicles_Data:
            regnum = line[REGISTRATION_NUMBER]
            if line[RENTED] == 'True':
                rented = True
            else:
                rented = False
            model_year = int(line[MODEL_YEAR])
            brand = line[BRAND]
            price = int(line[PRICE])
            car_type = int(line[CAR_TYPE])
            car = Vehicle(regnum, model_year, rented, brand, price, car_type)
            self.__Vehicles.append(car)

    def loadAvailableVehicles(self):
        for vehicle in self.__Vehicles:
            if not vehicle.isRented():
                self.__AvailableVehicles.append(vehicle)

    def loadRentedVehicles(self):
        for vehicle in self.__Vehicles:
            if vehicle.isRented():
                self.__VehiclesInRent.append(vehicle)

    def registerNewVehicle(self, registration_number, rented, model_year, brand, price, car_type):
        newVehicle = Vehicle(registration_number, model_year, rented, brand, price, car_type)
        self.__Vehicles.append(newVehicle)
        self.__Vehicles_Data.append([registration_number, rented, model_year, brand, price, car_type])
        self.save() #Save-a í hvert sinn sem við bætum við nýjum bíl
        return newVehicle

    def deregisterVehicle(self, registration_number):
        vehid = self.findVehicleID(registration_number)
        if vehid:
            self.__Vehicles.pop(vehid)
            self.__Vehicles_Data.pop(vehid)
            self.save()
        else:
            return None
            
    def findVehicleID(self, registration_number):
        for index, vehicle in enumerate(self.__Vehicles):
            if vehicle.getRegistrationNum() == registration_number:
                return index
        return None
    def getVehicles(self):
        return self.__Vehicles

    def getAvailable(self):
        return self.__AvailableVehicles
        
    def getRentedVehicles(self):
        return self.__VehiclesInRent

    def save(self):
        self.__DataSaver.writeVehicleData(self.__Vehicles_Data)
        
