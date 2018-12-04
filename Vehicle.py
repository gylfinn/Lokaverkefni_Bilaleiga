class Vehicle(object):
    def __init__(self, registration_num, model_year, rented=0):
        self.__registration_num = registration_num
        self.__model_year = model_year
        self.__rented = rented
    
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
    
    def __str__(self):
        return "{}, {}, {}".format(self.__model_year, self.__registration_num, self.__rented)


car1 = Vehicle("AB-523", 1995, 0)
car2 = Vehicle("AB-325", 2000, 1)
car3 = Vehicle("CD-523", 1998, 0)
car4 = Vehicle("DA-523", 1995, 1)
car5 = Vehicle("UT-523", 1993, 0)

print(car1)
print(car2)
print(car3)
print(car4)
print(car5)

car2.setModelYear(1503)
print(car2)

