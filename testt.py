x = int(input("Enter start number: "))
y = int(input("Enter a number: "))
for a in range(x, y+1):
    if a % a == 1:
        print(a)