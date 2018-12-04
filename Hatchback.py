class Hatchback(Vehicle):
    def __init__(self, brand, price):
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
