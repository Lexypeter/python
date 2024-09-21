#A traffic code
def func():
    print("""
Welcome to the traffic light choose a number 
1. Red
2. yellow
3. green
""")
    Enter = input("Enter a number:  ")
    if Enter == "1":
        print("Stop")
    elif Enter == "2":
        print("Slow down")
    elif Enter == "3":
        print("Go")
    else:
        print("Wrong number")

func()
