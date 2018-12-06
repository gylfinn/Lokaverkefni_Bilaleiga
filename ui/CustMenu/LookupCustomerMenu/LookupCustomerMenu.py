import os

def customerMenuSelection(self, check_if_admin, customer):
        selection = ""
        os.system('cls')
        while (selection !="9"):
            print(customer)
            print("1. Update information ")
            print("2. Customer Order History")
            if check_if_admin:
                print("3. Remove Customer")
            print("9. Go Back")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                print("1. Change Name ")
                print("2. Change SSN")
                print("3. Change Phone Number")
                print("4. Change Adress")
                print("5. Update Driver Licence ")
                action = input()
                os.system('cls')
                if action == "1":
                    replace_index = 0
                    name = input("Name: ")
                    self.__customer.changeInfo(customer, name, replace_index)
                    customer[0] = name
                    os.system('cls')
                elif action == "2":
                    replace_index = 1
                    SSN = input("SSN: ")
                    self.__customer.changeInfo(customer, SSN, replace_index)
                    customer[1] = SSN
                    os.system('cls')
                elif action == "3":
                    replace_index = 2
                    phone_number = input("Phone Number: ")
                    self.__customer.changeInfo(customer, phone_number, replace_index)
                    customer[2] = phone_number
                    os.system('cls')
                elif action == "4":
                    replace_index = 3
                    adress = input("Adress: ")
                    self.__customer.changeInfo(customer, adress, replace_index)
                    customer[3] = adress
                    os.system('cls')
                elif action == "5":
                    replace_index = 4
                    driver_license_number = input("Driver license number: ")
                    self.__customer.changeInfo(customer, driver_license_number, replace_index)
                    customer[4] = driver_license_number
                    os.system('cls')

            elif selection == "2":
                customer_ssn = customer[1]
                user_history = self.__order.findUserHistory(customer_ssn)
                for line in user_history:
                    print(line,end="\n")
            
            elif selection == "3" and check_if_admin:
                ssn = customer[1]
                self.__customer.deleteCustomer(customer, ssn)
                customer = None
                return customer