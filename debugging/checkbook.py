#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def read_amount(prompt):
    """Read a positive float amount from the user, reprompting on invalid input."""
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g., 10 or 10.50).")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        return amount

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = read_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = read_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
