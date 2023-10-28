import json

class BankingSystem:
    def _init_(self):
        self.accounts = {}  # Store account information in a dictionary

    def save_accounts_to_file(self):
        with open("accounts.json", "a") as file:
            json.dump(self.accounts, file)

    def load_accounts_from_file(self):
        self.accounts = {}  # Clear existing accounts
        try:
            with open("accounts.json", "r") as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            pass

    def open_new_account(self):
        # Calculate the account number based on the last account's number
        account_numbers = list(self.accounts.keys())
        if account_numbers:
            account_number = max(account_numbers) + 1
        else:
            account_number = 1

        name = input("Enter your name: ")
        balance = float(input("Enter the initial balance: "))
        password = input("Set a password: ")

        self.accounts[account_number] = {"name": name, "balance": balance, "password": password}
        print("Your new account's number is ", account_number)
        self.save_accounts_to_file()

    def login_to_existing_account(self):
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")

        if account_number in self.accounts:
            account_info = self.accounts[account_number]
            if account_info["password"] == password:
                print(f"Welcome, {account_info['name']}!")
                self.user_menu(account_number)
            else:
                print("Invalid password. Please try again.")
        else:
            print("Account not found. Please try again.")

    def user_menu(self, account_number):
        while True:
            choice = int(input("User Menu:\n"
                               "1. View Balance\n"
                               "2. Deposit\n"
                               "3. Withdraw\n"
                               "4. Change Password\n"
                               "5. Exit\n"
                               "Enter your choice: "))

            account_info = self.accounts[account_number]
            if choice == 1:
                print(f"Your balance: ${account_info['balance']:.2f}")
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                account_info["balance"] += amount
                self.save_accounts_to_file()
                print("Deposit successful.")
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                if amount > account_info["balance"]:
                    print("Insufficient balance.")
                else:
                    account_info["balance"] -= amount
                    self.save_accounts_to_file()
                    print("Withdrawal successful.")
            elif choice == 4:
                new_password = input("Enter a new password: ")
                account_info["password"] = new_password
                self.save_accounts_to_file()
                print("Password changed successfully.")
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "_main_":
    banking_system = BankingSystem()

    while True:
        b = int(input("**********************************************************************************************\n"
                       "*                                                                                            *\n"
                       "*                                                                                            *\n"
                       "*                               Welcome to the User Portal                                   *\n"
                       "*                                                                                            *\n"
                       "*                                    1. Open a new account                                   *\n"
                       "*                                                                                            *\n"
                       "*                                    2. Login to your existing account                       *\n"
                       "*                                                                                            *\n"
                       "*                                    3. Exit                                                 *\n"
                       "**********************************************************************************************\n"))
        if b == 1:
            banking_system.open_new_account()
        if b == 2:
            banking_system.login_to_existing_account()
        if b == 3:
            break
        else:
            print("Please Enter a Valid Input")