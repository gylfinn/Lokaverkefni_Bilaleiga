
from ui.OrderMenu.OrderMenu import OrderMenu
from ui.MainMenu import MainMenu
from ui.LoginMenu import LoginMenu
from services.VehicleManager import VehicleManger
from services.OrderManager import OrderManager
from ui.OrderMenu.LookupOrderMenu import LookupOrderMenu
from ui.OrderMenu.UpcomingOrders import UpcomingOrders
from ui.OrderMenu.NewOrder import NewOrder

EMPTY = "EMPTY"
LOGINMENU = "loginmenu"
MAINMENU = "mainmenu"
ORDERMENU = "ordermenu"
LOOKUPORDERMENU = "lookupordermenu"
UPCOMINGORDERS = "upcomingorders"
NEWORDER = "neworder"

#Menu manager sem sér um að ferðast á milli UI klasa.
#Er kallað á hann með location sem er klasinn sem á að fara í
class MenuManager:
    def __init__(self):
        self.__location = EMPTY
        self.__last_location = EMPTY
        self.__login_menu = LoginMenu(self)
        self.__main_menu = MainMenu(self)
        self.__order_menu = OrderMenu(self)
        self.__lookup_order_menu = LookupOrderMenu.LookupOrderMenu(self)
        self.__upcoming_orders = UpcomingOrders.UpcomingOrders(self)
        self.__new_order = NewOrder.NewOrder(self)
        self.__VehicleManager = VehicleManger()
        self.__OrderManager = OrderManager()


        #--Start up at login loaction--
        self.gotoClass(LOGINMENU)

    def isAdmin(self):
        return self.__login_menu.isadmin
    def getVehicleManger(self):
        return self.__VehicleManager
    def getOrderManager(self):
        return self.__OrderManager
    def gotoClass(self, location):
        self.__last_location = self.__location
        self.__location = location

        if self.__location == MAINMENU:
            self.__main_menu.main_menu()
        elif self.__location == LOGINMENU:
            self.__login_menu.login_menu()
        elif self.__location == ORDERMENU:
            self.__order_menu.orderMenu()
        elif self.__location == LOOKUPORDERMENU:
            self.__lookup_order_menu.lookupOrderMenu()
        elif self.__location == UPCOMINGORDERS:
            self.__upcoming_orders.upcomingOrders()
        elif self.__location == NEWORDER:
            self.__new_order.newOrder()

