from repo.GetCustomerData import GetCustomerData

class GetCustomerInfo:
    def __init__(self):
        self.__customer = GetCustomerData()
        self.__customer_data = self.__customer.readCustomerData()

    def getCustomer(self, ssn):
        for line in self.__customer_data:
            if ssn in line:
                return line