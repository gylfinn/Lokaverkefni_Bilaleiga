from repo.GetData import GetData
from repo.SaveData import SaveData
from Models.Order import Order

ORDER_FILE = "orders.csv"
class OrderManager(object):
    def __init__(self):
        self.__Orders_Data = GetData(ORDER_FILE).readData()
        self.__Orders = []
        self.__DataSaver = SaveData(ORDER_FILE)
        for order in self.__Orders_Data:
            newOrder = Order(order[0], order[1], order[2], order[3], order[4], order[5]) #TODO: Add constants
            self.__Orders.append(newOrder)
    
    def createOrder(self, order_id, car_reg, customer_SSN, date_from, date_to, price):
        newOrder = Order(order_id, car_reg, customer_SSN, date_from, date_to, price)
        self.__Orders.append(newOrder)
        self.__Orders_Data.append([order_id, car_reg, customer_SSN, date_from, date_to, price])
        self.Save()
        return newOrder
        
    def removeOrder(self, order_id):
        order_id -= 1 # Ekki nice en works
        self.__Orders.pop(order_id)
        self.__Orders_Data.pop(order_id)
    
    def getOrders(self, by_dates = False):
        if by_dates:
            return self.__Orders #TODO: Látta þetta virka
        else:
            return self.__Orders

    def findOrder(self, search_key): # Hægt að search ID, Registration Number og SSN
        for order in self.__Orders:
            if str(order.getOrderid()) == search_key:
                return order
            if str(order.getCarRegistration()) == search_key:
                return order
            if str(order.getCustomerSSN()) == search_key:
                return order
        return None #Ef ekkert order er found þá returnar hann none

    def Save(self):
        self.__DataSaver.WritOrdersData(self.__Orders_Data)