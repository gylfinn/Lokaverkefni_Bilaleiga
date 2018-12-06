import csv
class SaveData():
    def __init__(self, file_name):
        self.__file_name = "./data/" + file_name
    def WritOrdersData(self, Orders):
        file = open(self.__file_name, "w", newline = '')
        file.write("orderid,carregistrationnumber,customerssn,datefrom,dateto,totalprice\n")
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for order in Orders:
            writer.writerow(order)
        file.close()
    def WriteVehicleData(self, ehicle):
        pass #Add Later

