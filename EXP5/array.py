# Array / List
# Python commonly uses lists as arrays

numbers = [10, 20, 30, 40, 50]
print(numbers)


# Access Array Elements
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])


# Negative Indexing
# -1 represents the last element
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[-2])


# Array Traversal
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Taking Array Input
numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

print(numbers)


# Add Element using append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)


# Insert Element
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)


# Remove Element
# remove() removes a value
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)


# Remove Element using pop()
# pop() removes an element using its index
numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)


# Update Element
numbers = [10, 20, 30, 40]
numbers[2] = 35
print(numbers)


# Find Length
numbers = [10, 20, 30, 40]
print(len(numbers))


# Find Maximum and Minimum
numbers = [10, 50, 20, 80, 30]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# Find Sum
numbers = [10, 20, 30, 40]
print("Sum:", sum(numbers))


# Search Element
numbers = [10, 20, 30, 40]
search = int(input("Enter number to search: "))

if search in numbers:
    print("Element found")
else:
    print("Element not found")


# Sort Array
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)


# Sort in Descending Order
numbers = [50, 20, 40, 10, 30]
numbers.sort(reverse=True)
print(numbers)


# Reverse Array
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)


# Array Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])


# 2D Array
# A 2D array is a list inside another list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


# Access 2D Array Element
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print(matrix[1][2])


# Traverse 2D Array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# Array Module
# array module creates a typed array
from array import array

numbers = array('i', [10, 20, 30, 40])
print(numbers)


# Add Element to Array Module
from array import array

numbers = array('i', [10, 20, 30])
numbers.append(40)
print(numbers)