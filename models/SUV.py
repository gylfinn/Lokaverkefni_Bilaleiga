from Vehicle import Vehicle

class SUV(Vehicle):
    def __init__(self, registration_num, model_year, rented, brand, price):
        Vehicle.__init__(self, registration_num, model_year, rented)
        self.__brand = brand
        self.__price = int(price)
    
    def getBrand(self):
        return self.__brand

    def setBrand(self, new_brand):
        self.__brand = new_brand
        return self.__brand

    def getPrice(self):
        return self.__price

    def setPrice(self, new_price):
        self.__price = new_price
        return self.__price

    def __str__(self):
        return "Model year: {}, Registration number: {},Rented: {},Brand: {},Price {}".format(self.getRegistrationNum, self.getModelYear, self.getRented, self.getBrand, self.getPrice)

car1 = SUV("AB-251", 2000, 0, "Toyota", 150620)

print(car1)