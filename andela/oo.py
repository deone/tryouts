#!/usr/bin/env python

class BankAccount(object):

    def withdraw(self):
        pass

    def deposit(self):
        pass

class SavingsAccount(BankAccount):

    def __init__(self):
        self.balance = 500

    def deposit(self, amount):
        if amount < 0:
            return 'Invalid deposit amount'
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return 'Invalid withdraw amount'

        if amount > self.balance:
            return 'Cannot withdraw beyond the current account balance'

        balance = self.balance - amount
        if balance < 500:
            return 'Cannot withdraw beyond the minimum account balance'

        self.balance = balance
        return self.balance

class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return 'Invalid deposit amount.'
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return 'Invalid withdraw amount'

        if amount > self.balance:
            return 'Cannot withdraw beyond the current account balance'

        self.balance -= amount
        return self.balance
