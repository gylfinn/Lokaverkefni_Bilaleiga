from modules import *
from pynput.keyboard import Key, Listener

def login():
    while True:
        user_acc = False
        user_logged_in = False
        user_list = ['gylfi18']
        user_pw = ['12345']
        print("Sladu inn notendanafn")
        choice = input("> ")
        if choice in user_list:
            user_acc = True
        else:
            print("Invalid User\n")
        if user_acc == True:
            print("Sladu inn lykilord")
            lykilord = input("> ")
            if lykilord in user_pw:
                user_logged_in = True
                return user_logged_in
            else:
                print("Ekki rett lykilorð")


def main():
    user_logged_in = login()
    
main()
