from repo.GetData import GetData
from repo.SaveData import SaveData
from Models.Order import Order
from datetime import datetime

ORDER_FILE = "orders.csv"
ORDER_ID = 0
CAR_REG = 1
CUSTOMER_SSN = 2
DATE_FROM = 3
DATE_TO = 4
PRICE = 5

class OrderManager(object):
    def __init__(self):
        self.__Orders_Data = GetData(ORDER_FILE).readData()
        self.__Orders = []
        self.__DataSaver = SaveData(ORDER_FILE)
        for order in self.__Orders_Data:
            newOrder = Order(order[ORDER_ID], 
            order[CAR_REG], 
            order[CUSTOMER_SSN], 
            order[DATE_FROM], 
            order[DATE_TO], 
            order[PRICE])
            self.__Orders.append(newOrder)
    
    def createOrder(self, order_id, car_reg, customer_SSN, date_from, date_to, price):
        newOrder = Order(order_id, car_reg, customer_SSN, date_from, date_to, price)
        self.__Orders.append(newOrder)
        self.save()
        return newOrder
        
    def removeOrder(self, order):
        self.__Orders.remove(order)
        self.save()

    def updateOrderData(self):
        self.__Orders_Data.clear()
        for order in self.__Orders:
            self.__Orders_Data.append([order.getOrderid(), order.getCarRegistration(), order.getCustomerSSN(), datetime.strftime(order.getDateFrom(), "%d/%m/%y %H:%M"), datetime.strftime(order.getDateTo(), "%d/%m/%y %H:%M"), order.getPrice()])
    def getUpCommingOrders(self):
        sorted_orders = self.getOrders(by_dates=True)
        up_comming = list()
        for order in sorted_orders:
            if order.getDateFrom() > datetime.now():
                up_comming.append(order)
        return up_comming
    def getOrders(self, by_dates = False):
        if by_dates:
            sorted_orders = sorted(self.__Orders, key=lambda Order: Order.getDateFrom())
            return sorted_orders
        else:
            return self.__Orders
    def getOrdersByVehicle(self, reg_number):
        vehicle_history = list()
        for order in self.__Orders:
            if order.getCarRegistration().lower() == reg_number.lower():
                vehicle_history.append(order)
        return vehicle_history
    def getOrdersByCustomer(self, SSN):
        customer_history = list()
        for order in self.__Orders:
            if int(order.getCustomerSSN()) == int(SSN):
                customer_history.append(order)
        return customer_history
    def findOrder(self, search_key): # Hægt að search ID, Registration Number og SSN
        for order in self.__Orders:
            if str(order.getOrderid()) == search_key:
                return order
            if str(order.getCarRegistration()) == search_key:
                return order
            if str(order.getCustomerSSN()) == search_key:
                return order
        return None #Ef ekkert order er found þá returnar hann none

    def save(self):
        self.updateOrderData()
        self.__DataSaver.writeOrdersData(self.__Orders_Data)