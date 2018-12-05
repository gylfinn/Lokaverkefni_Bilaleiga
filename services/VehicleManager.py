from repo.GetData import GetData
from Models.Vehicle import Vehicle


class VehicleManger(object):
    def __init__(self):
        self.__Vehicles_Data = GetData("cars.csv").readData()
        self.__Vehicles = []
    def LoadVehicles(self):
        for line in self.__Vehicles_Data:
            regnum = line.split(',')[0]
            rented = line.split(',')[1]
            model_year = line.split(',')[2]
            brand = line.split(',')[3]
            price = line.split(',')[4]
            car_type = line.split(',')[5]
            car = Vehicle(regnum, model_year, rented, brand, price, car_type)
            self.__Vehicles.append(car)



