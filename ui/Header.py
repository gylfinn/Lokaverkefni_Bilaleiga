import time
import os

class Header:
    def __init__(self):
        self.__nextmenu = None
        self.__tree_list = []
        self.__isadmin = False
        self.__fullname = ""
    

    def GetLocation(self, location):
        dirlocation = "Main Menu"
        if location == "EMPTY":
            return dirlocation
        elif location == "mainmenu":
            return dirlocation
        elif location == "ordermenu":
            dirlocation = "Main Menu > Orders"

        elif location == "custmenu":
            dirlocation = "Main Menu > Customers"

        elif location == "carmenu":
            dirlocation = "Main Menu > Cars"

        elif location == "upcomingorders":
            dirlocation = "Main Menu > Orders > Upcoming orders"

        elif location == "neworder":
            dirlocation = "Main Menu > Orders > New Order"
            
        elif location == "lookupordermenu":
            dirlocation = "Main Menu > Orders > Lookup"

        elif location == "changeorder":
            dirlocation = "Main Menu > Orders > Lookup > Change order"
        elif location == "cancelorder":
            dirlocation = "Main Menu > Orders > Lookup > Cancel order"
        elif location == "pricecalculator":
            dirlocation = "Main Menu > Orders > Price Calculator"
        elif location == "fleetmenu":
            dirlocation = "Main Menu > Cars > Fleet"
        elif location == "caradministrationmenu":
            dirlocation = "Main Menu > Cars > Administration"
        elif location == "registernewcar":
            dirlocation = "Main Menu > Cars > Administration > Register"
        elif location == "deregistercar":
            dirlocation = "Main Menu > Cars > Administration > Deregister"
        elif location == "overview":
            dirlocation = "Main Menu > Cars > Fleet > Overview"
        elif location == "currentrentals":
            dirlocation = "Main Menu > Cars > Fleet > Current Rentals"
        elif location == "available":
            dirlocation = "Main Menu > Cars > Fleet > Available cars"
        elif location == "returncar":
            dirlocation = "Main Menu > Cars > Fleet > Return car"
        elif location == "rentcar":
            dirlocation = "Main Menu > Cars > Fleet > Rent car"
        elif location == "lookupcustomermenu":
            dirlocation = "Main Menu > Customers > Lookup"
        elif location == "registercustomer":
            dirlocation = "Main Menu > Customers > Register Customer"
        elif location == "updateinformation":
            dirlocation = "Main Menu > Customers > Lookup > Update"
        elif location == "":
            dirlocation = ""
        return dirlocation

    def printLoginHeader(self):
        os.system('cls||clear')
        print('-' * 75)
        print("{}{}".format("PLEASE LOG IN TO CONTINUE".ljust(30), time.ctime().rjust(30)))
        print('-' * 75)

    def printHeader(self, location):
        location = self.GetLocation(location)
        if self.__isadmin:
            admintag = "(A)"
        else:
            admintag = ""

        displayname = self.__fullname + admintag

        os.system('cls||clear')
        print('-' * 75)
        print("Welcome {}{}".format(displayname.ljust(30), time.ctime().rjust(30)))
        print('-' * 75)
        print(location)
        print('-' * 75)
        print("")

    def setIsAdmin(self, isadmin):
        if isadmin:
            self.__isadmin = True
        else:
            self.__isadmin = False

    def setFullname(self, fullname):
        self.__fullname = fullname

    def getNextMenu(self):
        return self.__nextmenu
    
    def setNextMenu(self, nextmenu):
        self.__nextmenu = nextmenu
        self.__tree_list.append(self.__nextmenu)
        
    def clearNextMenu(self):
        self.__nextmenu = None