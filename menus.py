def show_main_menu():
    print("1. Accounts")
    print("2. Transactions")
    print("3. Reports")
    print("4. Exit")

    ch = input("Enter Your Choice: ")
    if ch == 1:
        show_accounts_sub_menus()
    elif ch == 2:
        show_transactions_sub_menu()
    elif ch == 3:
        pass
    else:
        print("Thanks you for using BMS.")
        exit()


def show_accounts_sub_menus():
    print("Showing sub menus")


def show_transactions_sub_menu():
    print()
