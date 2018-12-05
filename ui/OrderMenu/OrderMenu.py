import os
from ui.MainMenu import MainMenu
from ui.OrderMenu.UpcomingOrders.UpcomingOrders import UpcomingOrders


class OrderMenu:
    def __init__(self, isadmin, username, fullname):
        self.isadmin = isadmin
        self.username = username
        self.fullname = fullname
    def order_menu(self):
        os.system('cls')
        order_menu_selection = ""
        while(order_menu_selection !="9"):
            print("Order Menu")
            print("1. Upcoming Orders")
            print("2. New Order")
            print("3. Look up order")
            print("8. Back")
            print("9. Log out")

            if order_menu_selection == "1":
                UpcomingOrders.upcoming_orders(self)
            elif order_menu_selection == "2":
                NewOrder.new_order(self)
            elif order_menu_selection == "3":
                LookupOrder.lookup_order(self)
            elif order_menu_selection =="8":
                MainMenu.main_menu(self)
            elif order_menu_selection == "9":
                MainMenu.main_menu(self)