import os
from ui.MainMenu import MainMenu
from ui.OrderMenu.UpcomingOrders.UpcomingOrders import UpcomingOrders
from ui.OrderMenu.NewOrder.NewOrder import NewOrder
from ui.OrderMenu.LookupOrder.LookupOrder import LookupOrder


#Þessi klasi þarf að kalla á klasa í services sem leitar að order
#og sýnir svo upplýsingar um þá order og býður notanda að velja 1,2,3
# fyrir cancel, change, chargeback
class LookupOrder:
    def __init__(self, isadmin, username, fullname):
        self.isadmin = isadmin
        self.username = username
        self.fullname = fullname

    def lookupOrder(self):
        os.system('cls')
        lookup_order_selection = ""
        while(lookup_order_selection !="9"):
            print("Order info displayed here")
            print("1. Change order")
            print("2. Cancel Order")
            print("3. Chargeback Order")
            print("8. Back")
            print("9. Log out")

            lookup_order_selection = input()

            if lookup_order_selection == "1":
                pass
                #Calls change order service class
            elif lookup_order_selection == "2":
                pass
                #Calls cancel order service class
            elif lookup_order_selection == "3":
                pass
                #calls chargeback order service class
            elif lookup_order_selection =="8":
                pass
                #Calls menuManager and calls the class behind this one
            elif lookup_order_selection == "9":
                pass
                #Calls menuManager MAINMENU