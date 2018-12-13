import os
from colorama import Fore
from Models.Order import Order

#Þessi klasi þarf að kalla á klasa í services sem leitar að order
#og sýnir svo upplýsingar um þá order og býður notanda að velja 1,2,3
# fyrir cancel, change, chargeback
class LookupOrderMenu:
    def __init__(self, manager):
        self.__manager = manager

    def lookupOrderMenu(self):
        self.__manager.printHeader()
        lookup_order_selection = ""
        order = self.__manager.getMetadata()
        order_id = input("Order ID: ")
        order = self.__manager.getOrderManager().findOrder(order_id)
        self.__manager.setMetadata(order)
        self.__manager.printHeader()

        while(lookup_order_selection !="9") and order != None:
            print(Fore.YELLOW, order, Fore.WHITE)
            print(Fore.GREEN,end="")
            print("1. Change order")
            print("2. Cancel Order")
            # print("3. Chargeback Order")
            print(Fore.RED,end="")
            print("9. Back")
            print(Fore.WHITE,end="")
            lookup_order_selection = input()

            if lookup_order_selection == "1":
                self.__manager.gotoClass("changeorder")
            elif lookup_order_selection == "2":
                self.__manager.gotoClass("cancelorder")
            # elif lookup_order_selection == "3":    
            #     self.__manager.gotoClass("chargebackorder")
            elif lookup_order_selection == "9":
                self.__manager.clearMetadata() #Setja Metadata aftur í None svo engir lúðar fari að nota það aftur xD:PXOXOXOXOX
                self.__manager.gotoClass("ordermenu")

        if order == None:
            print("Order Does Not Exist")
            print("1. Search Again")
            print("9. Go Back")
            selection = input()
            if selection == "1":
                self.__manager.gotoClass("lookupordermenu")
            else:
                self.__manager.gotoClass("ordermenu")