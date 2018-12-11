from datetime import datetime

class Order():
    def __init__(self, order_id, car_registration_number, customer_SSN, date_from, date_to, total_price):
        self.__order_id = order_id
        self.__car_registration_number = car_registration_number
        self.__customer_ssn = customer_SSN
        self.__date_from = datetime.strptime(date_from, "%d/%m/%y %H:%M") #21/11/06 16:30
        self.__date_to = datetime.strptime(date_to, "%d/%m/%y %H:%M")
        self.__total_price = total_price
    def getOrderid(self):
        return self.__order_id
    def getCarRegistration(self):
        return self.__car_registration_number
    def setCarRegistration(self, new_car_reg):
        self.__car_registration_number = new_car_reg
    def getCustomerSSN(self):
        return self.__customer_ssn
    def setCustomerSSN(self, new_ssn):
        self.__customer_ssn = new_ssn
    def getDateFrom(self):
        return self.__date_from
    def setDateFrom(self, new_date):
        self.__date_from = new_date
    def getDateTo(self):
        return self.__date_to
    def setDateTo(self, new_date):
        self.__date_to = new_date
    def getPrice(self):
        return self.__total_price
    def setPrice(self, new_price):
        self.__total_price = new_price

    def __gt__(self, other):
        return self.__date_from > other.date_from
    #def __repr__(self):
        #return [self.getOrderid(), self.getCarRegistration(), self.getCustomerSSN(), self.getDateFrom(), self.getDateTo(), self.getPrice()]
    def __str__(self):
        return "OrderID: {}, Car Registration: {} Customer SSN: {} Date: From {} to {}, Price:{}".format(self.getOrderid(), self.getCarRegistration(), self.getCustomerSSN(), self.getDateFrom(), self.getDateTo(), self.getPrice())
    
    
    
    