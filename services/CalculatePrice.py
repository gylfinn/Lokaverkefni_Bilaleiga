class CalculatePrice:
    def __init__(self):
        pass

    def calculatePrice(self, days, type_of_car):
        self.__days = days
        self.__type_of_car = type_of_car
        return self.__days * (self.__type_of_car*100)
