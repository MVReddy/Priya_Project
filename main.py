
import sys

from accounts.main_menu import MainMenu


class LoginMessage:

    def __init__(self):
        pass

    def login(self):
        count = 0
        with open("DB/credentials.txt", 'r') as f:
            data = [x.strip().split(':') for x in f.readlines()]
            print data
            l = len(data)
        while count<3:
            user_name = input("Enter user Name: ")
            password = input("Enter password: ")
            if [user_name,password] in data[0:l]:
                print("SUCCESSFULLY LOGGED INTO BMS")
                o = MainMenu
                o.main_menu()
            else:
                count += 1
                print("User name and password doesnt match.")
        else:
            print 'Please contact for Administrative Assistance'
            sys.exit()
