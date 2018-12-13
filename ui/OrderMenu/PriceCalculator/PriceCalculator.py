import os
from services.CalculatePrice import CalculatePrice
from colorama import Fore

class PriceCalculator: 
    def __init__(self, manager):
        self.__manager = manager
        self.__calculate_price = CalculatePrice()
    def priceCalculator(self): 
        self.__manager.printHeader()
        upcoming_order_menu_selection = ""
        while(upcoming_order_menu_selection !="9"):
            try:
                days = int(input("How many days? "))
                print("What type of car?")
                print(Fore.GREEN,end="")
                print("1. Hatchback")
                print("2. Sedan")
                print("3. SUV")
                print(Fore.WHITE,end="")
                type_of_car = int(input())
                price = self.__calculate_price.calculatePrice(days, type_of_car)
                self.__manager.printHeader()
                print("The Price of this Order would be {} dollars".format(price))
            except ValueError:
                print("Only enter numbers")
            print(Fore.GREEN,end="")
            print("Press 1 to calculate again ")
            print(Fore.RED,end="")
            print("Press any other key to go back\n")
            print(Fore.WHITE,end="")
            pricecalc_confirmation = input()
            if pricecalc_confirmation == "1":
                self.__manager.gotoClass("pricecalculator")
            else:
                self.__manager.gotoClass("ordermenu")
