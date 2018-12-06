
from ui.OrderMenu.OrderMenu import OrderMenu
from ui.MainMenu import MainMenu
from ui.OrderMenu.LookupOrderMenu.LookupOrderMenu import LookupOrderMenu
from ui.OrderMenu.NewOrder.NewOrder import NewOrder
from ui.OrderMenu.UpcomingOrders.UpcomingOrders import UpcomingOrders

MAINMENU = "mainmenu"
ORDERMENU = "ordermenu"
LOOKUPORDERMENU = "lookupordermenu"
UPCOMINGORDERS = "upcomingorders"
NEWORDER = "neworder"

#Menu manager sem sér um að ferðast á milli UI klasa.
#Er kallað á hann með location sem er klasinn sem á að fara í
class MenuManager:
    def __init__(self, location):
        self.__location = location
        self.__main_menu = MainMenu()
        self.__order_menu = OrderMenu()
        self.__lookup_order_menu = LookupOrderMenu()
        self.__upcoming_orders = UpcomingOrders()
        self.__new_order = NewOrder()

        #self.__is_admin = is_admin

    def gotoClass(self, location):
        if self.__location == MAINMENU:
            # MainMenu.mainMenu(self)
            self.__main_menu.mainMenu()
            pass
        elif self.__location == ORDERMENU:
            #OrderMenu.orderMenu(self)
            self.__order_menu.orderMenu()
        elif self.__location == LOOKUPORDERMENU:
            #LookupOrderMenu.lookupOrderMenu(self)
            self.__lookup_order_menu.lookupOrderMenu()
        elif self.__location == UPCOMINGORDERS:
            #UpcomingOrders.upcomingOrders(self)
            self.__upcoming_orders.upcomingOrders()
        elif self.__location == NEWORDER:
            #NewOrder.newOrder(self)
            self.__new_order.newOrder()

