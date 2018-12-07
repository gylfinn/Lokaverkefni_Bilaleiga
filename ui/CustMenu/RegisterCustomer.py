from services.Customer import Customer
import os

class RegisterCustomer:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()
        
    def registerCustomer(self):
        os.system('cls')
        name = input("Name: ")
        SSN = input("SSN: ")
        adress = input("Adress: ")
        phonenumber = input("Phone number: ")
        driver_license_number = input("Driver License number: ")
        self.__customer.registerCustomer(name, SSN, adress, phonenumber, driver_license_number)