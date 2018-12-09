from repo.GetOrderData import GetOrderData

#Ætti að vera undir Models en er þegar komið 
class Order:
    def __init__(self):
        self.__order = GetOrderData()
        self.__order_data = self.__order.readOrderData()

    def findUserHistory(self, customerssn):
        user_list = []
        for line in self.__order_data:
            if customerssn in line:
                user_list.append(line)
            else:
                pass
        return user_list
    
    def registerOrder(self, orderid, carregistrationnumber, customerssn, datefrom, dateto, totalprice):
        self.__order_data.registerOrder(orderid, carregistrationnumber, customerssn, datefrom, dateto, totalprice)