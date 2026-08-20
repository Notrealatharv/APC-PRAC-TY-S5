"""
Python Data Types and Operations with Result Display
"""

print("="*60)
print("1. INTEGER DATA TYPE")
print("="*60)
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("\n" + "="*60)
print("2. FLOAT DATA TYPE")
print("="*60)
x = 7.5
y = 2.3
print(f"x = {x}, y = {y}")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Floor Division: {x} // {y} = {x // y}")

print("\n" + "="*60)
print("3. STRING DATA TYPE")
print("="*60)
str1 = "Hello"
str2 = "Python"
print(f"str1 = '{str1}', str2 = '{str2}'")
print(f"Concatenation: '{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")
print(f"Repetition: '{str1}' * 3 = '{str1 * 3}'")
print(f"Length: len('{str1}') = {len(str1)}")
print(f"Uppercase: '{str1}'.upper() = '{str1.upper()}'")
print(f"Lowercase: '{str1}'.lower() = '{str1.lower()}'")
print(f"First character: '{str1}'[0] = '{str1[0]}'")
print(f"Slice: '{str1}'[1:4] = '{str1[1:4]}'")
print(f"Replace: '{str1}'.replace('H', 'J') = '{str1.replace('H', 'J')}'")
print(f"Split: 'Hello World'.split() = {'Hello World'.split()}")

print("\n" + "="*60)
print("4. BOOLEAN DATA TYPE")
print("="*60)
bool1 = True
bool2 = False
print(f"bool1 = {bool1}, bool2 = {bool2}")
print(f"AND: {bool1} and {bool2} = {bool1 and bool2}")
print(f"OR: {bool1} or {bool2} = {bool1 or bool2}")
print(f"NOT: not {bool1} = {not bool1}")
print(f"NOT: not {bool2} = {not bool2}")

print("\n" + "="*60)
print("5. LIST DATA TYPE")
print("="*60)
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'hello', 3.14, True]
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 (mixed) = {list3}")
print(f"Length: len(list1) = {len(list1)}")
print(f"First element: list1[0] = {list1[0]}")
print(f"Last element: list1[-1] = {list1[-1]}")
print(f"Slice: list1[1:4] = {list1[1:4]}")
list1.append(6)
print(f"After append(6): list1 = {list1}")
list1.extend([7, 8])
print(f"After extend([7, 8]): list1 = {list1}")
list1.insert(0, 0)
print(f"After insert(0, 0): list1 = {list1}")
list1.remove(0)
print(f"After remove(0): list1 = {list1}")
popped = list1.pop()
print(f"After pop(): removed {popped}, list1 = {list1}")
print(f"Concatenation: {[1, 2]} + {[3, 4]} = {[1, 2] + [3, 4]}")
print(f"Repetition: {[1, 2]} * 2 = {[1, 2] * 2}")

print("\n" + "="*60)
print("6. TUPLE DATA TYPE")
print("="*60)
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('x', 'y', 'z')
tuple3 = (1, 'hello', 3.14, True)
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
print(f"tuple3 (mixed) = {tuple3}")
print(f"Length: len(tuple1) = {len(tuple1)}")
print(f"First element: tuple1[0] = {tuple1[0]}")
print(f"Last element: tuple1[-1] = {tuple1[-1]}")
print(f"Slice: tuple1[1:4] = {tuple1[1:4]}")
print(f"Concatenation: {(1, 2)} + {(3, 4)} = {(1, 2) + (3, 4)}")
print(f"Repetition: {(1, 2)} * 2 = {(1, 2) * 2}")
print(f"Count 2 in tuple1: tuple1.count(2) = {tuple1.count(2)}")
print(f"Index of 3 in tuple1: tuple1.index(3) = {tuple1.index(3)}")

print("\n" + "="*60)
print("7. DICTIONARY DATA TYPE")
print("="*60)
dict1 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"Access value: dict1['name'] = {dict1['name']}")
print(f"Length: len(dict1) = {len(dict1)}")
print(f"Keys: dict1.keys() = {list(dict1.keys())}")
print(f"Values: dict1.values() = {list(dict1.values())}")
print(f"Items: dict1.items() = {list(dict1.items())}")
dict1['email'] = 'john@example.com'
print(f"After adding 'email': dict1 = {dict1}")
dict1.update({'age': 26, 'country': 'USA'})
print(f"After update: dict1 = {dict1}")
removed_value = dict1.pop('email')
print(f"After pop('email'): removed '{removed_value}', dict1 = {dict1}")

print("\n" + "="*60)
print("8. SET DATA TYPE")
print("="*60)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {'a', 'b', 'c'}
print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set3 = {set3}")
print(f"Length: len(set1) = {len(set1)}")
set1.add(6)
print(f"After add(6): set1 = {set1}")
set1.remove(6)
print(f"After remove(6): set1 = {set1}")
print(f"Union: {set1} | {set2} = {set1 | set2}")
print(f"Intersection: {set1} & {set2} = {set1 & set2}")
print(f"Difference: {set1} - {set2} = {set1 - set2}")
print(f"Symmetric Difference: {set1} ^ {set2} = {set1 ^ set2}")
print(f"Is subset: {1, 2} <= {set1} = {(1, 2).__le__(set1) if isinstance((1, 2), set) else '{1, 2}.issubset(set1) =' + str(set({1, 2}).issubset(set1))}")

print("\n" + "="*60)
print("9. COMPARISON OPERATIONS")
print("="*60)
num1, num2 = 10, 5
print(f"num1 = {num1}, num2 = {num2}")
print(f"Equal: {num1} == {num2} = {num1 == num2}")
print(f"Not Equal: {num1} != {num2} = {num1 != num2}")
print(f"Greater than: {num1} > {num2} = {num1 > num2}")
print(f"Less than: {num1} < {num2} = {num1 < num2}")
print(f"Greater than or equal: {num1} >= {num2} = {num1 >= num2}")
print(f"Less than or equal: {num1} <= {num2} = {num1 <= num2}")

print("\n" + "="*60)
print("10. TYPE CONVERSION")
print("="*60)
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(123) = '{str(123)}'")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"list((1, 2, 3)) = {list((1, 2, 3))}")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3, 3]) = {set([1, 2, 2, 3, 3])}")

print("\n" + "="*60)
print("11. MIXED TYPE OPERATIONS")
print("="*60)
mixed_list = [10, 3.14, 'Python', True, [1, 2], {'key': 'value'}]
print(f"mixed_list = {mixed_list}")
print(f"Length: {len(mixed_list)}")
for i, item in enumerate(mixed_list):
    print(f"  Index {i}: {item} (type: {type(item).__name__})")

print("\n" + "="*60)
print("Script Completed Successfully!")
print("="*60)
