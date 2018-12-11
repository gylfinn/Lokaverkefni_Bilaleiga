import os
from services.CalculatePrice import CalculatePrice

class PriceCalculator: 
    def __init__(self, manager):
        self.__manager = manager
        self.__calculate_price = CalculatePrice()
    def priceCalculator(self): 
        os.system('cls')
        upcoming_order_menu_selection = ""
        while(upcoming_order_menu_selection !="9"):
            try:
                days = int(input("How many days? "))
                print("What type of car?")
                print("1. Hatchback")
                print("2. Sedan")
                print("3. SUV")
                type_of_car = int(input())
                price = self.__calculate_price.calculatePrice(days, type_of_car)
                os.system('cls')
                print("The Price of this Order would be {} dollars".format(price))
            except ValueError:
                print("Only enter numbers")

            print("Press 1 to calculate again, any other key to go back\n")
            pricecalc_confirmation = input()
            if pricecalc_confirmation == "1":
                self.__manager.gotoClass("pricecalculator")
            else:
                self.__manager.gotoClass("ordermenu")