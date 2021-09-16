#!/usr/bin/env python3

class BankAccount:
    
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount

    def Withdrawal(self, amount):
        if amount > self.balance:
            print("There is no enough money for withdrawing {amount}")
            self.display()
        else: 
            self.balance -= amount

    def bankFees(self, BANK_FEE = 5):
        self.balance -= self.balance * BANK_FEE / 100

    def display(self):
        print("Account number:", self.accountNumber)
        print("Client name:", self.name)
        print("Account balance:", self.balance)

my_account = BankAccount(1234567890, "Ani", 0)
my_account.Deposit(100)
my_account.Withdrawal(50)
my_account.Withdrawal(1000)
