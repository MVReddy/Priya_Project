# import menus
from menus import *


credentials = {'admin': 'pass123', 'user1': 'abcd'}


def login():
    count = 0

    while count < 3:
        user_name = input("Enter user Name: ")
        password = input("Enter password: ")

        if user_name in credentials:
            if password == credentials.get(user_name):
                print("SUCCESSFULLY LOGGED INTO BMS")
                show_main_menu()
                break
            else:
                count += 1
                print("User name and password doesn;t match.")
        else:
            print("User doesn't exisit")
    else:
        print("Your Account got locked. Please contact Admin")


def my_login(user_name, password):
    count = 0

    while count < 3:
        if user_name in credentials:
            if password == credentials.get(user_name):
                print("SUCCESSFULLY LOGGED INTO BMS")
                show_main_menu()
                break
            else:
                count += 1
                print("User name and password doesn;t match.")
        else:
            print("User doesn't exisit")
    else:
        print("Your Account got locked. Please contact Admin")

def sum(a, b):
    return a+b
