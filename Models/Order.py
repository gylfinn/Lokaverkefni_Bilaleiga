from datetime import datetime

class Order():
    def __init__(self, order_id, car_registration_number, customer_SSN, date_from, date_to, total_price):
        self.__order_id = order_id
        self.__car_registration_number = car_registration_number
        self.__customer_ssn = customer_SSN
        self.__date_from = datetime(date_from)
        self.__date_to = datetime(date_to)
        self.__total_price = total_price
    def getOrderid(self):
        return self.__order_id
    def getCarRegistration(self):
        return self.__car_registration_number
    def getCustomerSSN(self):
        return self.__customer_ssn
    def getDateFrom(self):
        return self.__date_from
    def getDateTo(self):
        return self.__date_to
    def getPrice(self):
        return self.__total_price
    def __gt__(self, other):
        return self.__date_from > other.date_from
    def __str__(self):
        return "OrderID: {}, Car Registration: {} Customer SSN: {} Date: From {} to {}, Price:{}".format(self.getOrderid(), self.getCarRegistration(), self.getCustomerSSN(), self.getDateFrom(), self.getDateTo(), self.getPrice())
    
    
    
    