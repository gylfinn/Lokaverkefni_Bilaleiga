from services.Customer import Customer
from services.servicehelpers.Validator import Validator
import os

class RegisterCustomer:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()
        self.__validator = Validator()
        
    def registerCustomer(self):
        os.system('cls')
        name = input("Name: ")
        SSN = input("SSN: ")
        adress = input("Address: ")
        phonenumber = input("Phone number: ")
        driver_license_number = input("Driver License number: ")
        self.__customer.registerCustomer(name, SSN, adress, phonenumber, driver_license_number)
        os.system('cls')
        if self.__validator.ValidateSSN(SSN):
            print("{}, SSN: {} registered succesfully!".format(name, SSN))
            print("Press 1 to register another one, any other key to go back\n")
            regcust_confirmation = input()
            if regcust_confirmation == "1":
                self.__manager.gotoClass("registercustomer")
            else:
                self.__manager.gotoClass("custmenu")
        else:
            print("Registration failed. SSN is not valid")
            print("Press any key to go back")
            regcust_confirmation = input()
            self.__manager.gotoClass("custmenu")