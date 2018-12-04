import csv
import os
# Til að fá root path verkefnisins
dirname = os.path.realpath(".")
# Síðann absaloutpath á user.csv skránna
user_file = os.path.join(dirname, '/data/users.csv')

class GetUserData:
    def readData(user_file):
        with open (user_file, "r") as user_file:
            csv_reader = csv.reader(user_file)
            for line in csv_reader:
                print(line)

    readData(user_file)
    



