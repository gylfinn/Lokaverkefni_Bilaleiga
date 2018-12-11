import os
from services.servicehelpers.Validator import Validator

#Þessi klasi kallar tekur við info um nýtt order, sendir það svo til services sem skrifar í Repo layer
#Á líka að geta tekið við daga fjölda og týpu af bíl og sent til services sem reiknar út
#verðið svo hægt sé að segja vv það

class NewOrder:
    def __init__(self, manager):
        self.__manager = manager

    def newOrder(self):
        os.system('cls')
        new_order_menu_selection = ""
        while(new_order_menu_selection !="9"):
            orderid = input("Order Id: ")
            car_regnum = input("Car Registration Number: ")
            customer_ssn = input("Customer SSN: ")
            date_from = input("Date From: ")
            date_to = input("Date To: ")
            total_price = input("Total price: ")
            new_order = self.__manager.getOrderManager().createOrder(orderid, car_regnum, customer_ssn, date_from, date_to, total_price)
            print(new_order)
            print("9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("ordermenu")