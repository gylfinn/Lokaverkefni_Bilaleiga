import os
from ui.MainMenu import MainMenu
from ui.OrderMenu import OrderMenu

#Þessi klasi kallar tekur við info um nýtt order, sendir það svo til services sem skrifar í Repo layer

class NewOrder:
    def __init__(self, isadmin, username, fullname):
        self.isadmin = isadmin
        self.username = username
        self.fullname = fullname
    def newOrder(self):
        os.system('cls')
        new_order_menu_selection = ""
        while(new_order_menu_selection !="9"):
            print("New order is recieved here, needs work")
            print("9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
               pass