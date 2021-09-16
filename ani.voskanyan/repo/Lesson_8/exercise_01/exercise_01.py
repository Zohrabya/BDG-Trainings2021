#!/usr/bin/env python3

class BankAccount:
    
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def bankfees(self, BANK_FEE = 5):
        self.balance -= self.balance * BANK_FEE / 100

    def display(self):
        print(self.account_number)
        print(self.name)
        print(self.balance)

try:
    account_number = int(input("Enter your account number: "))
except ValueError:
    print("Wrong input. Account number should have numeric type. Try again.")
    account_number = int(input("Enter your account number: "))

try:    
    name = input("Enter your name: ")
except:
    print("Wrong input. Name should have string type. Try again.")

balance = input("Enter your initial balance")

if type(account_number) != int or type(name) != str:
    raise ValueError("Wrong input type")

my_account = BankAccount(account_number, name, int(balance))
my_account.display()
