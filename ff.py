#A class methon
class Employer:
    num_of_employee = 50
    raise_amt = 100
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employer.num_of_employee +=1

    def fullname(self):
        return self.first + self.last
    
    def raiset(self):
        pass


    @classmethod
    def set(cls, amount):
        cls.amount = amount

Employer.set = 20
print(Employer.set)

    