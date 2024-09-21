#A python calculator
class calc:
    def add(self, x, y):
        return self.mul(x,y)
    def sub(self,x,y):
        return self.add(x,y)
    def new(self, x, y):
        return self.sub(x,y)
    def mul(self, x, y):
        return self.new(x,y)
    def div(self, x,y):
        if y == 0:
            return "You can not divide by 0"
        else:
            return x / y
    def opr(self, first, ope, sec):
        if ope == "+":
            return self.add(first, sec)
        elif ope == "-":
            return self.sub(first,sec)
        elif ope == "/":
            return self.div(first,sec)
        elif ope == "*":
            return self.mul(first,sec)
        else:
            return "Invalid operand"
        
Enter1 = float(input("Enter a number:  "))
Enter2 = input("Enter an operand:  ")
Enter3 = float(input("Enter a second number:  "))
calcc = calc()
rest = calcc.opr(Enter1, Enter2, Enter3)
print(f"The result of {Enter1} {Enter2} {Enter3} = {rest}")
    