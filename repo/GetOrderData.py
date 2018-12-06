import csv

class GetOrderData: 
    def __init__(self):
        self.__orderdata = []

    def readData(self):
        with open ("./data/orders.csv", "r") as order_file:
            csv_reader = csv.reader(order_file)
            next(csv_reader)
            for line in csv_reader:
                self.__orderdata.append(line)
        return self.__orderdata