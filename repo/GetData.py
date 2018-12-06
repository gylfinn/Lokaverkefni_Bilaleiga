import csv

class GetData: 
    def __init__(self, file_name):
        self.__data = []
        self.__file_name = "./data/" + file_name
    
    def readData(self):
        f = open(self.__file_name, "r")
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            self.__data.append(line)
        return self.__data