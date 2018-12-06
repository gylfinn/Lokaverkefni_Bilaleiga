import csv

class GetCustomerData:
    def __init__(self):
        self.__customer_data = []

    def readCustomerData(self):
        with open ("./data/customers.csv", "r") as customer_file:
            csv_reader = csv.reader(customer_file)
            next(csv_reader)
            for line in csv_reader:
                self.__customer_data.append(line)
        return self.__customer_data

    def register_customer(self, name, ssn, adress, phonenumber, driver_license_number):
        with open ("./data/customers.csv", "a+", newline="") as customer_file:
            customer_writer = csv.writer(customer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            customer_writer.writerow([name, ssn, adress, phonenumber, driver_license_number])

    def changeCustomerInfo(self, customer, name, replace_index):
        new_list = []
        with open("./data/customers.csv", "r") as customer_file_r:
            reader = csv.reader(customer_file_r)
            for line in reader:
                if customer == line:
                    customer[replace_index] = name
                    new_list.append(customer)
                elif line != "":
                    new_list.append(line)

        with open ("./data/customers.csv", "w", newline="") as customer_file_w:
            writer = csv.writer(customer_file_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in new_list:
                writer.writerow(line)

    def deleteCustomer(self, customer, ssn):
        new_list = []
        with open("./data/customers.csv", "r") as customer_file_r:
            reader = csv.reader(customer_file_r)
            for line in reader:
                if customer == line:
                    pass
                else:
                    new_list.append(line)
        
        with open("./data/customers.csv", "w", newline="") as customer_file_w:
            writer = csv.writer(customer_file_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in new_list:
                writer.writerow(row)