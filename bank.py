#A python class to get account balance
class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be more than 0")
    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -+ amount
        else:
            print("Insufficient balance or withdraw")

    def getbalance(self):
        return self.balance

    

    

    

        

