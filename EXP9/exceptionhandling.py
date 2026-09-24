# 1. BASIC TRY-EXCEPT
# try = code that may cause an error
# except = handles the error

try:
    a = 10
    b = 0
    print(a / b)

except:
    print("Error occurred")

# 2. ZERO DIVISION ERROR
# Handles division by zero

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# 3. VALUE ERROR
# Happens when invalid value is converted

try:
    age = int("abc")
    print(age)

except ValueError:
    print("Invalid value")


# 4. TYPE ERROR
# Happens when incompatible data types are used

try:
    result = 10 + "5"
    print(result)

except TypeError:
    print("Cannot add integer and string")


# 5. MULTIPLE EXCEPTIONS
# Different errors can be handled separately

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# 6. EXCEPTION OBJECT
# 'as e' stores the error message

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError as e:
    print("Error:", e)


# 7. TRY-EXCEPT-ELSE
# else runs only when there is NO error

try:
    a = 10
    b = 0
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)


# 8. TRY-EXCEPT-FINALLY
# finally ALWAYS executes

try:
    a = 10
    b = 2
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")

# 9. TRY-EXCEPT-ELSE-FINALLY
# Complete exception handling structure

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("This always executes")

# 10. CUSTOM ERROR USING raise
# raise is used to create an error manually

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")


# 11. CUSTOM ERROR WITH try-except
# We can create our own error message using raise

try:
    marks = 30

    if marks < 40:
        raise ValueError("Student has failed")

    print("Student has passed")

except ValueError as e:
    print("Error:", e)


#12. USER-DEFINED EXCEPTION
# Create our own exception class
# Custom exception should inherit from Exception

class AgeError(Exception):
    pass


try:
    age = 15

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Eligible")

except AgeError as e:
    print("Custom Error:", e)