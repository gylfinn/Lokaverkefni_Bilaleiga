from services.CustomerManager import CustomerManager  
import os
from colorama import Fore

class UpdateInformation:
    def __init__(self, manager):
        self.__manager = manager
    def updateInformation(self):
        self.__manager.printHeader()
        information_to_update = ""
        customer = self.__manager.getMetadata()
        print(customer)
        while(information_to_update != "9"):
            print("\n1. Change customer ", customer.getName())
            print(Fore.RED, "***Leaving field empty will keep the default the value***", Fore.WHITE)
            print("2. Change SSN")
            customer.setSSN(input() or customer.getSSN())
            print("3. Change Address")
            customer.setAddress(input() or customer.getAddress())
            print("4. Change Phone Number")
            customer.setPhoneNumber(input() or customer.getPhoneNumber())
            print("5. Change Driver license number")
            customer.setDriversLicenseNumber(input() or customer.getDriversLicenseNumber())
            print(customer)
            print(Fore.GREEN, "1. Confirm Changes", Fore.WHITE)
            print(Fore.RED, "9. Cancel Changes / Go Back", Fore.WHITE)
            information_to_update = input()
            if information_to_update == "9":
                self.__manager.gotoClass("custmenu")
            elif information_to_update == "1":
                self.__manager.getCustomerManager().save()
                self.__manager.gotoClass("custmenu")
                