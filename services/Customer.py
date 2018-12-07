from repo.GetCustomerData import GetCustomerData
from services.servicehelpers.GetCustomerInfo import GetCustomerInfo
import os

class Customer:
    def __init__(self):
        self.__customer_data = GetCustomerData()
        self.__customer_info = GetCustomerInfo()

    def registerCustomer(self):
        os.system('cls')
        name = input("Name: ")
        SSN = input("SSN: ")
        adress = input("Adress: ")
        phonenumber = input("Phone number: ")
        driver_license_number = input("Driver License number: ")
        self.__customer_data.register_customer(name, SSN, adress, phonenumber, driver_license_number)

    def lookUpCustomer(self, ssn):
        customer = self.__customer_info.getCustomer(ssn)
        return customer

    def changeInfo(self, customer, name, replace_index):
        self.__customer_data.changeCustomerInfo(customer, name, replace_index)
    
    def deleteCustomer(self, customer, ssn):
        self.__customer_data.deleteCustomer(customer, ssn)