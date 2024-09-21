class Account:
    def __init__(self, account, balance, pin):
        self.balance = balance
        self.account = account
        self.__pin = pin

    def _getBalance(self):
        if self.account == "0774286095" and self.__pin == "1770":
            return self.balance
        else:
            return "Invalid parameter"
        
new1 = input("Enter account number:  ")
new2 = 20000
new3 = input("Enter account pin:  ")
calc = Account(new1, new2, new3)
print(f" Your account balance is {calc._getBalance()}")
