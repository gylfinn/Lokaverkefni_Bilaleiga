from ui.MainMenu import MainMenu
from ui.LoginMenu import LoginMenu

from services.VehicleManager import VehicleManger
from services.OrderManager import OrderManager

from ui.OrderMenu.OrderMenu import OrderMenu
from ui.OrderMenu.LookupOrderMenu import LookupOrderMenu
from ui.OrderMenu.LookupOrderMenu.CancelOrder import CancelOrder
from ui.OrderMenu.LookupOrderMenu.ChangeOrder import ChangeOrder
from ui.OrderMenu.LookupOrderMenu.ChargebackOrder import ChargebackOrder
from ui.OrderMenu.UpcomingOrders import UpcomingOrders
from ui.OrderMenu.NewOrder import NewOrder

from ui.CustMenu.CustMenu import CustMenu
from ui.CustMenu.LookupCustomerMenu.LookupCustomerMenu import LookupCustomerMenu
from ui.CustMenu.LookupCustomerMenu.UpdateInformation import UpdateInformation
from ui.CustMenu.LookUpCustomer import LookUpCustomer
from ui.CustMenu.RegisterCustomer import RegisterCustomer

from ui.CarMenu.CarMenu import CarMenu
from ui.CarMenu.CarAdministrationMenu.CarAdministrationMenu import CarAdministrationMenu
from ui.CarMenu.CarAdministrationMenu.DeregisterCar import DeregisterCar
from ui.CarMenu.CarAdministrationMenu.RegisterNewCar import RegisterNewCar


EMPTY = "EMPTY"
CANCELORDER = "cancelorder"
CHANGEORDER = "changeorder"
CHARGEBACKORDER = "chargebackorder"
LOOKUPCUSTOMER = "lookupcustomer"
REGISTERCUSTOMER = "registercustomer"
LOGINMENU = "loginmenu"
MAINMENU = "mainmenu"
ORDERMENU = "ordermenu"
LOOKUPORDERMENU = "lookupordermenu"
UPCOMINGORDERS = "upcomingorders"
NEWORDER = "neworder"
CUSTMENU = "custmenu"
LOOKUPCUSTOMERMENU = "lookupcustomermenu"
UPDATEINFORMATION = "updateinformation"
CARMENU = "carmenu"
CARADMINISTRATIONMENU = "caradministration"
DEREGISTERCAR = "deregistercar"
REGISTERNEWCAR = "registernewcar"
AVAILABLE = "available"
CURRENTRENTALS = "currentrentals"
OVERVIEW = "overview"

#Menu manager sem sér um að ferðast á milli UI klasa.
#Er kallað á hann með location sem er klasinn sem á að fara í
class MenuManager:
    def __init__(self):
        self.__location = EMPTY
        self.__last_location = EMPTY
        self.__login_menu = LoginMenu(self)
        self.__main_menu = MainMenu(self)
        self.__order_menu = OrderMenu(self)
        self.__cust_menu = CustMenu(self)
        self.__lookup_order_menu = LookupOrderMenu.LookupOrderMenu(self)
        self.__upcoming_orders = UpcomingOrders.UpcomingOrders(self)
        self.__new_order = NewOrder.NewOrder(self)
        self.__VehicleManager = VehicleManger()
        self.__OrderManager = OrderManager()
        self.__lookup_customer_menu = LookupCustomerMenu(self)
        self.__update_information = UpdateInformation(self)
        self.__look_up_customer = LookUpCustomer(self)
        self.__register_customer = RegisterCustomer(self)
        self.__cancel_order = CancelOrder(self)
        self.__change_order = ChangeOrder(self)
        self.__chargeback_order = ChargebackOrder(self)
        self.__car_menu = CarMenu(self)
        self.__car_administration_menu = CarAdministrationMenu(self)
        self.__register_new_car_menu = RegisterNewCar(self)
        self.__deregister_car_menu = DeregisterCar(self)


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
        elif self.__location == LOOKUPCUSTOMERMENU:
            self.__lookup_customer_menu.lookupCustomerMenu()
        elif self.__location == CUSTMENU:
            self.__cust_menu.customerMenu()
        elif self.__location == UPDATEINFORMATION:
            self.__update_information.updateInformation()
        elif self.__location == REGISTERCUSTOMER:
            self.__register_customer.registerCustomer()
        elif self.__location == LOOKUPCUSTOMER:
            self.__look_up_customer.lookupCustomer()
        elif self.__location == CANCELORDER:
            self.__cancel_order.cancelOrder()
        elif self.__location == CHANGEORDER:
            self.__change_order.changeOrder()
        elif self.__location == CHARGEBACKORDER:
            self.__chargeback_order.chargebackOrder()
        elif self.__location == CARMENU:
            self.__car_menu.carMenu()
        elif self.__location == CARADMINISTRATIONMENU:
            self.__car_administration_menu.carAdministrationMenu()
        elif self.__location == REGISTERNEWCAR:
            self.__register_new_car_menu.registerNewCar()
        elif self.__location == DEREGISTERCAR:
            self.__deregister_car_menu.deregisterCar()