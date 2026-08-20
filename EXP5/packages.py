# 1. Import Package
import mypackage

print("Package imported successfully")


# 2. Import Module
from mypackage import calculator

print("Addition:", calculator.add(10, 5))
print("Multiplication:", calculator.multiply(10, 5))


# 3. Import Function
from mypackage.calculator import subtract

print("Subtraction:", subtract(10, 5))