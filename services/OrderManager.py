from repo.GetData import GetData
class OrderManager(object):
    def __init__(self):
        self.__Orders_Data = GetData("orders.csv").readData()
        self.__Orders = []
        for order in self.__Orders_Data:
            print(order) # Fix