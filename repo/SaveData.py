import csv
class SaveData():
    def __init__(self, file_name):
        self.__file_name = "./data/" + file_name
    def WriteData(self, data):
        file = open(self.__file_name, "a+")
        w = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in data:
            w.writerow(item)
