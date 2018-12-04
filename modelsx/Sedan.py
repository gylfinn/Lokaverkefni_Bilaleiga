from Vehicle import Vehicle

class Sedan(Vehicle):
    def __init__(self, registration_num, model_year, rented, brand, price):
        super().__init__(self, registration_num, model_year, rented)
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
        return "{} {} {} {} {}".format(self.getRegistrationNum, self.getModelYear, self.getRented, self.getBrand, self.getPrice)


car1 = Sedan("AB-251", 2000, 0, "Toyota", 150620)

print(car1)
