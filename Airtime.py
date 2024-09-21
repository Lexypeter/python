#A program which works like a bank ussd
def func():
    try:
        print("Welcome to the USSD Application!\n  1.Check Balance\n  2.Buy Airtime\n  3.Exit")
        Enter1 =int(input("Please enter your choice:"))
        if Enter1 > 0 and Enter1 < 4:
            if Enter1 == 1:
                print("Your account balance is:$100")
                return func()
            elif Enter1 == 2:
                Enter2 = int(input("Enter the amount to buy airtime:"))
                print("You have successfully purchased $" + str(Enter2) + " airtime.")
                return func()
            else:
                 print("Thank you for using our service. Goodbye!")
        else:
            return func()
    except ValueError:
        print("PLEASE ENTER A NUMBER")
        return func()

print(func())