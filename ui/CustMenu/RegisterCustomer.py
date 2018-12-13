
from services.servicehelpers.Validator import Validator
import os

class RegisterCustomer:
    def __init__(self, manager):
        self.__manager = manager
        self.__validator = Validator()
        
    def registerCustomer(self):
        self.__manager.printHeader()
        name = input("Name: ")
        SSN = input("SSN: ")
        address = input("Address: ")
        phone_number = input("Phone number: ")
        driver_license_number = input("Driver License number: ")
        self.__manager.printHeader()
        if self.__validator.ValidateSSN(SSN):
            self.__manager.getCustomerManager().registerNewCustomer(name, SSN, address, phone_number, driver_license_number)
            print("{}, SSN: {} registered succesfully!".format(name, SSN))
            print("Press 1 to register another customer. Press any other key to go back\n")
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