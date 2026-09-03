# Constructor
# __init__() is automatically called when an object is created

class Student:
    def __init__(self):
        print("Constructor called")

student1 = Student()


# Constructor with Parameters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Atharv", 20)

print("Name:", student1.name)
print("Age:", student1.age)


# Constructor with Default Arguments
class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

student1 = Student()
student2 = Student("Atharv", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)


# Constructor with Multiple Objects
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Atharv")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)


# Constructor with Class Variable
class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Atharv")

print("Name:", student1.name)
print("College:", student1.college)


# Constructor with Calculation
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

r = Rectangle(10, 5)

print("Area:", r.area())


# Destructor
# __del__() is called when an object is destroyed

class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

student1 = Student()

del student1


# Constructor and Destructor Together
class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")
        print("Student:", self.name)

    def __del__(self):
        print("Destructor called")

student1 = Student("Atharv")

del student1


# Destructor with Multiple Objects
class Student:
    def __init__(self, name):
        self.name = name
        print("Created:", self.name)

    def __del__(self):
        print("Destroyed:", self.name)

student1 = Student("Atharv")
student2 = Student("Rahul")

del student1
del student2