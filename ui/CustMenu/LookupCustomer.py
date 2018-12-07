from services.Customer import Customer

class LookUpCustomer:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def lookupCustomer(self):
        SSN = input("SSN: ")
        customer = self.__customer.lookUpCustomer(SSN)
        if customer != None:
            self.__manager.gotoclass("lookupcustomermenu")
        else:
            print("Customer does not exist")