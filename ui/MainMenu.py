import os

class MainMenu:



    def header(self, check_if_admin, username,):
        if check_if_admin:
            admintag = "(A)"
        else:
            admintag = ""
        print("------------------------------------")
        print("Welcome {}{} {}".format(username, admintag, time.ctime()))
        return

    def mainMenu(self, check_if_admin, username):
        os.system('cls')
        selection = ""
        while(selection !="9"):
            LoginMenu.header(self, check_if_admin, username)
            print("Main Menu")
            print("1. Order")
            print("2. Cars")
            print("3. Customers")
            print("9. Log out")
            print("--------------")
            selection = input()
            os.system('cls')

            if selection == "1":
                Interface.orderMenu(self)
            elif selection == "2":
                Interface.carMenu(self, check_if_admin)
            elif selection == "3":
                Interface.customerMenu(self, check_if_admin)
            elif selection == "9":
                Interface.loginScreen(self)