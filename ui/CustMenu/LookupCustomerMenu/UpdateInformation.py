from services.Customer import Customer  
import os       

class UpdateInformation:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = Customer()

    def updateInformation(self):
        customer = self.__manager.getMetadata()
        print("1. Change Name ")
        print("2. Change SSN")
        print("3. Change Phone Number")
        print("4. Change Adress")
        print("5. Update Driver Licence ")
        action = input()
        os.system('cls')
        if action == "1" and customer:
            replace_index = 0
            name = input("Name: ")
            self.__manager.customer.changeInfo(customer, name, replace_index)
            customer[0] = name
            os.system('cls')
        elif action == "2" and customer:
            replace_index = 1
            SSN = input("SSN: ")
            self.__customer.changeInfo(customer, SSN, replace_index)
            customer[1] = SSN
            os.system('cls')
        elif action == "3" and customer:
            replace_index = 2
            phone_number = input("Phone Number: ")
            self.__customer.changeInfo(customer, phone_number, replace_index)
            customer[2] = phone_number
            os.system('cls')
        elif action == "4" and customer:
            replace_index = 3
            adress = input("Adress: ")
            self.__customer.changeInfo(customer, adress, replace_index)
            customer[3] = adress
            os.system('cls')
        elif action == "5" and customer:
            replace_index = 4
            driver_license_number = input("Driver license number: ")
            self.__customer.changeInfo(customer, driver_license_number, replace_index)
            customer[4] = driver_license_number
            os.system('cls')
        self.__manager.setMetadata(None)