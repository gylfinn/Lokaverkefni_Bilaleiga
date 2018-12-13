import os
from colorama import Fore

# Þessi klasi spyr notandann hvort hann vilji confirma cancel order eða ekki
# ef hann velur YES þá er callað í service klasa sem eyðir orderinu
# ef nei, þá bara til baka

class CancelOrder:
    def __init__(self, manager):
        self.__manager = manager

    def cancelOrder(self):
        self.__manager.printHeader()
        cancel_order_menu_selection = ""
        order = self.__manager.getMetadata()
        while(cancel_order_menu_selection !="9"):
            print("Are you sure you want to cancel this order?")
            print("1. Yes")
            print("2. No")
            print("9. Back")
            cancel_order_menu_selection = input()
            if cancel_order_menu_selection == "9":
                self.__manager.gotoClass("lookupordermenu")
            elif cancel_order_menu_selection == "1":
                self.__manager.getVehicleManager().changeVehicleStatus(order.getCarRegistration())
                self.__manager.getOrderManager().removeOrder(order)
                self.__manager.clearMetadata()
                self.__manager.gotoClass("ordermenu")
            elif cancel_order_menu_selection == "2":
                self.__manager.gotoClass("lookupordermenu")