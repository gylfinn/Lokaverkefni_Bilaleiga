import os
from services.servicehelpers.Validator import Validator
from datetime import datetime
from colorama import Fore

#Þessi klasi kallar tekur við info um nýtt order, sendir það svo til services sem skrifar í Repo layer
#Á líka að geta tekið við daga fjölda og týpu af bíl og sent til services sem reiknar út
#verðið svo hægt sé að segja vv það

class NewOrder:
    def __init__(self, manager):
        self.__manager = manager

    def newOrder(self):
        self.__manager.printHeader()
        new_order_menu_selection = ""
        while(new_order_menu_selection !="9"):
            orderid = int(self.__manager.getOrderManager().getOrders()[-1].getOrderid())
            orderid += 1
            vehicle = None
            while vehicle == None:
                car_regnum = input("Car Registration Number: ")
                vehicle = self.__manager.getVehicleManager().findVehicle(car_regnum)
                if not vehicle:
                    print("Cannot find vehicle")
                    print(Fore.GREEN,end="")
                    print("1. Try Again")
                    print(Fore.RED,end="")
                    print("9. Go Back")
                    print(Fore.WHITE,end="")
                    selection = input()
                    if selection == "1":
                        self.__manager.gotoClass("neworder")
                    else:
                        self.__manager.gotoClass("ordermenu")
                if vehicle and vehicle.isRented():
                    print("Vehicle is not available")
                    print(Fore.GREEN,end="")
                    print("1. Try Again")
                    print(Fore.RED,end="")
                    print("9. Go Back")
                    print(Fore.WHITE,end="")
                    selection = input()
                    if selection == "1":
                        self.__manager.gotoClass("neworder")
                    else:
                        self.__manager.gotoClass("ordermenu")

            print(Fore.BLUE, vehicle, Fore.WHITE)
            customer = None
            while not customer:
                customer_ssn = input("Customer SSN: ")
                customer = self.__manager.getCustomerManager().findCustomer(customer_ssn)
                if not customer:
                    print(Fore.RED, "Cannot find customer with SSN '{}'".format(customer_ssn),Fore.WHITE)
                    ans = input("Do you want to register a new customer? (Y/N)")
                    if ans.lower() == "y":
                        self.__manager.gotoClass("registercustomer")
            print(Fore.YELLOW, customer, Fore.WHITE)

            date_from_validation = None
            while not date_from_validation:
                date_from = input("Date From: (dd/mm/yy hh:mm)\n")
                try:
                    date_from_validation = datetime.strptime(date_from, "%d/%m/%y %H:%M")
                except ValueError as e:
                    date_from_validation = None
                    print(Fore.RED, e)

            date_to_validation = None
            while not date_to_validation:
                date_to = input("Date To: (dd/mm/yy hh:mm)\n")
                try:
                    date_to_validation = datetime.strptime(date_to, "%d/%m/%y %H:%M")
                except ValueError as e:
                    date_to_validation = None
                    print(Fore.RED, e)
            total_price = input("Total price: ")
            new_order = self.__manager.getOrderManager().createOrder(orderid, car_regnum, customer_ssn, date_from, date_to, total_price)
            if new_order:
                self.__manager.getVehicleManager().changeVehicleStatus(car_regnum)
            self.__manager.printHeader()
            print(new_order)
            print("9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("ordermenu")