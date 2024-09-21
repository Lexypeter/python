#A function which outputs the wages of 
def func():
   wages = float(input("Enter your wages: "))
   hours = float(input("Enter number of hours: "))
   calc = wages * hours
   if wages > 0 and hours > 0:
      print(f" you worked for {hours} hours\n Your hourly payment is {wages}$\n Total wages earned = {calc}$")
   else:
     print("You are not eligible for any salary")

func()
