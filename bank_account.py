class BankAccount:

    def __init__(self, balance: float or int, name: str, account_number: int):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, withdrawal: int or float):
        if self.balance >= withdrawal:
            self.balance -= withdrawal
        else:
            raise ValueError("Insufficient Funds")
    
    def deposit(self, deposit: int or float):
        if deposit > 0:
            self.balance += deposit
        else:
            raise ValueError("Cannot deposit debt into the account")

    def print_balance(self):
        print(self.balance)
