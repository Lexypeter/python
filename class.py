#This is a file which displays a python the radius or area of a rectangle or circle
class Shape:
    new = 400
    def area(self):
        print(self.new)
        return "Calculating area"
        
        
class Rectangle(Shape):
   def __init__(self, x, y):
       self.x = x
       self.y = y
   
   def area(self):
       print(self.x * self.y)

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      

    def area(self):
      print(3.14 * self.radius)

p1 = Rectangle(20,30)
p2 = Circle(10)
p1.area()
p2.area()
Shape.new = 200
print(Shape.new)
