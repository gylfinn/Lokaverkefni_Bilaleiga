from repo.GetData import GetData
from Models.Order import Order

class OrderManager(object):
    def __init__(self):
        self.__Orders_Data = GetData("orders.csv").readData()
        self.__Orders = []
        for order in self.__Orders_Data:
            newOrder = Order(order[0], order[1], order[2], order[3], order[4], order[5])
            self.__Orders.append(newOrder)
    
    def createOrder(self, order_id, car_reg, customer_SSN, date_from, date_to, price):
        newOrder = Order(order_id, car_reg, customer_SSN, date_from, date_to, price)
        self.__Orders.append(newOrder)
        return newOrder
        
    def removeOrder(self, order_id):
        self.__Orders.pop(order_id)
    
    def getOrders(self, by_dates = False):
        if by_dates:
            return self.__Orders #TODO
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
        pass # Save-a öllum order í csv skrá eftir notkun