from Models.Order import Order
import os

# Þessi klasi spyr notanda hvort hann vilji chargebacka order
# ef hann confirmar þá er kallað í service class
# ef hann gerir back þá fer hann back duh

class ChargebackOrder:
    def __init__(self, manager):
        self.__manager = manager
    def chargebackOrder(self):
        os.system('cls')
        chargeback_order_menu_selection = ""
        order = self.__manager.getMetadata() #orderiið sem var flett upp i lookuporder a undan
        while(chargeback_order_menu_selection !="9"):
            print("Chargeback order:", order.getOrderid())
            print("SSN: ", order.getCustomerSSN())
            print("Date from: ", order.getDateFrom())
            print("Date to: ", order.getDateTo())
            print("Car Registration Number: ", order.getCarRegistration())
            print("1. Confirm chargeback ?")
            print("9. Back")
            chargeback_order_menu_selection = input()
            if chargeback_order_menu_selection == "9":
                self.__manager.gotoClass("lookupordermenu")
            elif chargeback_order_menu_selection == "1":
                self.__manager.getOrderManager().removeOrder(int(order.getOrderid()))
                #call service class here