#functions
def greet():
    print("Hello Atharv")
greet()

#Function with Parameters
def greet(name):
    print("Hello", name)
greet("Atharv")
greet("Rahul")

#Multiple Parameters
def add(a, b):
    print(a + b)
add(10, 20)

#Function with return
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

#Function with No Parameters and No Return
def message():
    print("Welcome to Python")
message()

# Parameters but No Return
def square(n):
    print(n * n)
square(5)

# Parameters + Return
def square(n):
    return n * n
result = square(5)
print(result)

# Default Arguments
def greet(name="Atharv"):
    print("Hello", name)    
greet()
greet("Rahul")

# Keyword argument
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=20, name="Atharv")

# Function Calling Another Function
def square(n):
    return n * n
def display(n):
    result = square(n)
    print(result)
display(5)

# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))