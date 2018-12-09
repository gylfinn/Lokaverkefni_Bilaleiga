class Vehicle(object):
    def __init__(self, registration_num, model_year, rented, brand, price, car_type):
        self.__registration_num = registration_num
        self.__model_year = model_year
        self.__rented = rented
        self.__brand = brand
        self.__price = price
        self.__type = car_type
    
    def getRegistrationNum(self):
        return self.__registration_num
        
    def setRegistrationNum(self, new_registration_num):
        self.__registration_num = new_registration_num

    def getModelYear(self):
        return self.__model_year

    def setModelYear(self, new_model_year):
        self.__model_year = new_model_year
    
    def isRented(self):
        return self.__rented
    
    def setRented(self, new_rented):
        self.__rented = new_rented

    def getPrice(self):
        return self.__price

    def setPrice(self, new_price):
        self.__price = new_price

    def getBrand(self):
        return self.__brand

    def setBrand(self, new_brand):
        self.__brand = new_brand
    
    def getType(self):
        return self.__type
    def __str__(self):
        return "Model year: {}, Registration number: {},Rented: {},Brand: {},Price {}".format(self.getModelYear(), self.getRegistrationNum(), self.isRented(), self.getBrand(), self.getPrice())