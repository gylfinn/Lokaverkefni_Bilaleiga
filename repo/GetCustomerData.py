import csv

class GetCustomerData:
    def __init__(self):
        self.__customer_data = []

    def readCustomerData(self):#Gætir notað bara GetData og SaveData
        with open ("./data/customers.csv", "r") as customer_file:
            csv_reader = csv.reader(customer_file)
            next(csv_reader)
            for line in csv_reader:
                self.__customer_data.append(line)
        return self.__customer_data

    def register_customer(self, name, ssn, adress, phonenumber, driver_license_number):
        with open ("./data/customers.csv", "a+") as customer_file:
            customer_writer = csv.writer(customer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            customer_writer.writerow([name, ssn, adress, phonenumber, driver_license_number])