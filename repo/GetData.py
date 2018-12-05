import csv

class GetData: 
    def __init__(self, file_name):
        self.__data = []
        self.__file_name = "./data/" + file_name

    def readData(self):
        with open (self.__file_name, "r") as user_file:
            csv_reader = csv.reader(user_file)
            next(csv_reader)
            for line in csv_reader:
                self.__data.append(line)
        return self.__data