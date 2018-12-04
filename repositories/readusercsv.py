import csv

class GetUserData:
    def __init__(self):
        self.userdata = []

    def readData(self):
        with open ("data/users.csv", "r") as user_file:
            csv_reader = csv.reader(user_file)
            for line in csv_reader:
                self.userdata.append(line)
        return self.userdata







    



