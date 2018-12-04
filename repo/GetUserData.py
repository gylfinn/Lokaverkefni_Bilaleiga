import csv

class GetUserData: 
    def __init__(self):
        self.__userdata = []

    def readData(self):
        with open ("./data/users.csv", "r") as user_file:
            csv_reader = csv.reader(user_file)
            next(csv_reader)
            for line in csv_reader:
                self.__userdata.append(line)
        return self.__userdata


    



 