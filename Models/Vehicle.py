class Vehicle(object):
    def __init__(self, registration_num, model_year, brand, price):
        self.__registration_num = registration_num
        self.__model_year = model_year
        self.__rented = 0
        self.__brand = brand
        self.__price = price
    
    def getRegistrationNum(self):
        return self.__registration_num
        
    def setRegistrationNum(self, new_registration_num):
        self.__registration_num = new_registration_num
        return self.__registration_num

    def getModelYear(self):
        return self.__model_year

    def setModelYear(self, new_model_year):
        self.__model_year = new_model_year
        return self.__model_year
    
    def getRented(self):
        return self.__rented
    
    def setRented(self, new_rented):
        self.__rented = new_rented
        return self.__rented

    def getPrice(self):
        return self.__price

    def setPrice(self, new_price):
        self.__price = new_price

    def getBrand(self):
        return self.__brand

    def setBrand(self, new_brand):
        self.__brand = new_brand
    
    def __str__(self):
        return "Model year: {}, Registration number: {},Rented: {},Brand: {},Price {}".format(self.getRegistrationNum(), self.getModelYear(), self.getRented(), self.getBrand(), self.getPrice())

'''class Sedan(Vehicle):
    def __init__(self, registration_num, model_year, brand, price):
        super().__init__(registration_num, model_year, brand, price)

class Hatchback(Vehicle):
    def __init__(self, registration_num, model_year, brand, price):
        super().__init__(registration_num, model_year, brand, price)

class SUV(Vehicle):
    def __init__(self, registration_num, model_year, brand, price):
        super().__init__(registration_num, model_year, brand, price)'''

