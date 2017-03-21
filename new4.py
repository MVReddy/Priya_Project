from app_login import login
from accounts.account import Test
from transactions import transaction


def show_welcome_message():
    print('*'*30)
    print("WELCOME TO BMS")
    print('*'*30)


if __name__ == '__main__':
    show_welcome_message()
    login()
    t = Test()
    t.my_test()
