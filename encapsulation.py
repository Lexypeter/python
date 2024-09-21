#An encapsulation file
class BankAccount:
    def __init__(self, number, name, balance):

        self.__number = number
        self.__name = name
        self.__balance = balance

    def get_withdraw(self, amount):
        if amount < self.__balance and amount > 0:
             return self.__balance - amount
        else:
            return " Invalid transaction" + self.__name + "please confirm if this account number is correct " + self.__number
            
    def set_withdraw(self, amount):
        return self.__balance + amount
    
        

aco = BankAccount(177021777, "Anyebe peter", 5000)
amount = int(input("Enter an amount: "))
print(aco.get_withdraw(amount))
print(aco.__number)
            
