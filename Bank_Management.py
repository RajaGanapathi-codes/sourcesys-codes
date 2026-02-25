import json
import os


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance
        }


class BankSystem:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def generate_account_number(self):
        return str(len(self.accounts) + 1)

    def create_account(self):
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial deposit: "))
        acc_no = self.generate_account_number()

        account = BankAccount(acc_no, name, balance)
        self.accounts[acc_no] = account.to_dict()
        self.save_data()

        print("Account created successfully!")

    def view_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return

        for acc_no, data in self.accounts.items():
            print(f"\nAccount No: {acc_no}")
            print(f"Name: {data['name']}")
            print(f"Balance: {data['balance']}")

    def deposit_money(self):
        acc_no = input("Enter account number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter deposit amount: "))
            self.accounts[acc_no]["balance"] += amount
            self.save_data()
            print("Amount deposited successfully!")
        else:
            print("Account not found.")

    def withdraw_money(self):
        acc_no = input("Enter account number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= self.accounts[acc_no]["balance"]:
                self.accounts[acc_no]["balance"] -= amount
                self.save_data()
                print("Amount withdrawn successfully!")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def delete_account(self):
        acc_no = input("Enter account number to delete: ")
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            self.save_data()
            print("Account deleted successfully!")
        else:
            print("Account not found.")


def main():
    system = BankSystem()

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.create_account()
        elif choice == "2":
            system.view_accounts()
        elif choice == "3":
            system.deposit_money()
        elif choice == "4":
            system.withdraw_money()
        elif choice == "5":
            system.delete_account()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()