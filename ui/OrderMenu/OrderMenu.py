import os
from ui.MenuManager import MenuManager

#This class is only 
class OrderMenu:
    def __init__(self):
        pass
        # self.isadmin = isadmin
        # self.username = username
        # self.fullname = fullname
    def orderMenu(self):
        os.system('cls')
        order_menu_selection = ""
        while(order_menu_selection !="9"):
            print("Order Menu")
            print("1. Upcoming Orders")
            print("2. New Order")
            print("3. Look up order")
            print("9. Back")

            if order_menu_selection == "1":
                MenuManager.gotoClass("upcomingorders")
            elif order_menu_selection == "2":
                MenuManager.gotoClass("neworder")
            elif order_menu_selection == "3":
                MenuManager.gotoClass("lookuporders")
            elif order_menu_selection =="9":
                MenuManager.gotoClass("mainmenu")
