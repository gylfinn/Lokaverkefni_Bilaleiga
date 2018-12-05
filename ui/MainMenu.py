import os

class MainMenu:
    def __init__(self, isadmin, username, fullname):
        self.isadmin = isadmin
        self.username = username
        self.fullname = fullname
    def main_menu(self):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            print("Main Menu")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print("9. Log out")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                #OrderMenu.order_menu()
                pass
            elif selection == "2":
                #Interface.carMenu(self, check_if_admin)
                pass
            elif selection == "3":
                #Interface.customerMenu(self, check_if_admin)
                pass
            elif selection == "9":
                #Interface.loginScreen(self)
                pass