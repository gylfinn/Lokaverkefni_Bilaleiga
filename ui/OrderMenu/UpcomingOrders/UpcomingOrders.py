import os
from ui.MainMenu import MainMenu


class UpcomingOrders:
    def __init__(self, isadmin, username, fullname):
        self.isadmin = isadmin
        self.username = username
        self.fullname = fullname
    def upcoming_orders(self):
        os.system('cls')
        order_menu_selection = ""
        while(order_menu_selection !="9"):