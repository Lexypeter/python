# class file
class StudentClass:
    def __init__(x,y,z):
        x.y = y
        x.z = z
    def func(x):
        hello = x.y * x.z
        return hello
class StudentChild(StudentClass):
    pass

p1 = StudentChild(20,40)
print(p1.func())
print(p1.y)

