from repo.GetData import GetData
from repo.SaveData import SaveData
from Models.Customer import Customer

NAME = 0
SSN = 1
ADDRESS = 2
PHONENUMBER = 3
DRIVERSLICENSENUMBER = 4
CUSTOMERS_FILE = "customer.csv"
class CustomerManager(object):
    def __init__(self):
        self.__customer_data = GetData(CUSTOMERS_FILE).readData()
        self.__customers = []
        self.__data_saver = SaveData(CUSTOMERS_FILE)
        self.loadCustomers()
    def save(self):
        self.updateCustomerData()
        self.__data_saver.writeCustomersData(self.__customer_data)
    def loadCustomers(self):
        for line in self.__customer_data:
            name = line[NAME]
            ssn = int(line[SSN])
            address = line[ADDRESS]
            phone_number = int(line[PHONENUMBER])
            driverslicense_number = int(line([DRIVERSLICENSENUMBER]))
            customer = Customer(name, ssn, address, phone_number,driverslicense_number)
            self.__customers.append(customer)
    def registerNewCustomer(self, name, ssn, address, phone_number, driverslicense_number):
        new_customer = Customer(name, ssn, address, phone_number, driverslicense_number)
        self.__customers.append(new_customer)
        self.save()
        return new_customer
    def removeCustomer(self, customer):
        self.__customers.remove(customer)
        self.save()
    def updateCustomerData(self):
        self.__customer_data.clear()
        for cust in self.__customers:
            self.__customer_data.append([cust.getName(), cust.getSSN(), cust.getAddress(), cust.getPhoneNumber(), cust.getPhoneNumber(), cust.getDriversLicenseNumber()])
    def findCustomer(self, search_key): #hægt að leita að name, ssn 
        for cust in self.__customers:
            if str(cust.getName()) == search_key:
                return cust
            if str(cust.getSSN()) == search_key:
                return cust
        return None #ef engin kúnni finnst
    

    
