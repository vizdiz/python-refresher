class BankAccount:

    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, withdrawal):
        if (self.balance >= withdrawal):
            self.balance -= withdrawal
    
    def deposit(self, deposit):
        self.balance += deposit

    def print_balance(self):
        print(self.balance)
