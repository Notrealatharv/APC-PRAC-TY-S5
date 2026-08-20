# Importing a Module
import math_operations
print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))

# from module import function
from math_operations import add
print(add(10, 5))

# Import Multiple Functions
from math_operations import add, subtract
print(add(10, 5))
print(subtract(10, 5))

# Import Everything
from math_operations import *
print(add(10, 5))
print(subtract(10, 5))

# Import with an Alias
import math_operations as m
print(m.add(10, 5))
print(m.subtract(10, 5))

# Built-in Modules
import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

# random Module
import random
number = random.randint(1, 10)
print(number)

names = ["Atharv", "Rahul", "Priya", "Amit"]
print(random.choice(names))

# os Module
import os

print(os.getcwd())
print(os.listdir())

# own module
'calculator.py'
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
print(calculator.square(6))