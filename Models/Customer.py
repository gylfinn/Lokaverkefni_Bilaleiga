class Customer:
    def __init__(self, name, ssn, address, phone_number, driverslicense_number):
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__phone_number = phone_number 
        self.__driverslicense_number = driverslicense_number
    def getName(self):
        return self.__name
    def getSSN(self):
        return self.__ssn
    def setSSN(self, new_ssn):
        self.__ssn = new_ssn
    def getAddress(self):
        return self.__address
    def setAddress(self, new_address):
        self.__address = new_address
    def getPhoneNumber(self):
        return self.__phone_number
    def setPhoneNumber(self, new_phone_number):
        self.__phone_number = new_phone_number
    def getDriversLicenseNumber(self):
        return self.__driverslicense_number
    def setDriversLicenseNumber(self, new_driverslicense_number):
        self.__driverslicense_number = new_driverslicense_number
    
    def __str__(self):
        return "Name: {}, SSN: {}, Address: {}, Phone number: {}, Driverslicense number: {}".format(self.getName(), self.getSSN(), self.getAddress(), self.getPhoneNumber(), self.getDriversLicenseNumber())
