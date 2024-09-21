#This program takes two numbers from the user and output the even numberrange between them
def func(input1, input2):
    count = 0
    for a in range(input1, input2 + 1):
        if a % 2 == 0:
            count +=1
    return (f"There are {count}  even numbers between {input1} and {input2}.")
input1 = int(input("Enter starting number: "))
input2= int(input("Enter End number: "))
print(func(input1,input2))