

class GetOrderData:
    def __init__(self):
        self.__order_data = []

    def readCustomerData(self):
        with open ("./data/orders.csv", "r") as order_file:
            csv_reader = csv.reader(order_file)
            next(csv_reader)
            for line in csv_reader:
                self.__order_data.append(line)
        return self.__order_data

    def newOrder(self, orderid, carregistrationnumber, customerssn, datefrom, dateto, totalprice):
        with open ("./data/orders.csv", "a+", newline="") as order_file:
            order_writer = csv.writer(order_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            order_writer.writerow([orderid, carregistrationnumber, customerssn, datefrom, dateto, totalpricev])

    def changeCustomerInfo(self, order, name, replace_index):
        new_list = []
        with open("./data/orders.csv", "r") as order_file_r:
            reader = csv.reader(order_file_r)
            for line in reader:
                if order == line:
                    customer[replace_index] = name
                    new_list.append(order)
                elif line != "":
                    new_list.append(order)
                else:
                    pass

        with open ("./data/orders.csv", "w", newline="") as order_file_w:
            writer = csv.writer(order_file_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in new_list:
                writer.writerow(line)

    def deleteCustomer(self, order, orderid):
        new_list = []
        with open("./data/orders.csv", "r") as order_file_r:
            reader = csv.reader(order_file_r)
            for line in reader:
                if order == line:
                    pass
                else:
                    new_list.append(line)
        
        with open("./data/orders.csv", "w", newline="") as order_file_w:
            writer = csv.writer(order_file_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in new_list:
                writer.writerow(row)