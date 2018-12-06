import os
from ui.MenuManager import MenuManager

#Þessi klasi kallar tekur við info um nýtt order, sendir það svo til services sem skrifar í Repo layer
#Á líka að geta tekið við daga fjölda og týpu af bíl og sent til services sem reiknar út
#verðið svo hægt sé að segja vv það

class NewOrder:
    def __init__(self):
        pass
        # self.isadmin = isadmin
        # self.username = username
        # self.fullname = fullname
    def newOrder(self):
        os.system('cls')
        new_order_menu_selection = ""
        while(new_order_menu_selection !="9"):
            print("New order is recieved here, needs work")
            print("9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                MenuManager.gotoClass("ordermenu")