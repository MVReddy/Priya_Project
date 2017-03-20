from accounts.sub_accounts_menu import SubAccounts
from reports.sub_reports_menu import SubReports
from transactions.sub_trasc_menu import SubTransaction


class MainMenu:
    def __init__(self):
        pass


    def main_menu(self):
        print("1. Accounts")
        print("2. Transactions")
        print("3. Reports")
        print("4. Exit")
        inp = int(raw_input('Enter select from main menu:'))
        if inp in range(1,5):
            if inp == 1:
                o = SubAccounts()
                o.sub_accounts()
            elif inp == 2:
                o1 = SubReports()
                o1.sub_trasc()
            elif inp == 3:
                o2 = SubTransaction
                o2.sub_reports()

        else:
            print ' Select valid one from main menu'

# o1 = MainMenu()
# o1.main_menu()
