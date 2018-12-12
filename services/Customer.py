# from repo.GetCustomerData import GetCustomerData
# from services.servicehelpers.GetCustomerInfo import GetCustomerInfo
# import os

# #Ætti að vera undir Models
# class Customer:
#     def __init__(self):
#         self.__customer_data = GetCustomerData()
#         self.__customer_info = GetCustomerInfo()

#     def registerCustomer(self, name, SSN, adress, phonenumber, driver_license_number):
#         self.__customer_data.register_customer(name, SSN, adress, phonenumber, driver_license_number)

#     def lookUpCustomer(self, ssn):
#         customer = self.__customer_info.getCustomer(ssn)
#         return customer

#     def changeInfo(self, customer, name, replace_index):
#         self.__customer_data.changeCustomerInfo(customer, name, replace_index)
    
#     def deleteCustomer(self, customer, ssn):
#         self.__customer_data.deleteCustomer(customer, ssn)