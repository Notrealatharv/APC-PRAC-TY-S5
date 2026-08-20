# one argument 
'normal function'
def square(x):
    return x * x
print(square(5))

'lambda function'
square=lambda x:x**2
print(square(5))

# 2arguments
add=lambda a,b:a+b
print(add(1,2))

multiply = lambda a, b: a * b
print(multiply(5, 4))

#without storing
print((lambda x:x**2)(4))

#lambda using if else
'syntax'':''lambda :x''condition if true''if' 'condition''else' 'cond if false'
check=lambda x:"even" if x%2==0 else "odd"
print(check(4))
print(check(5))

#Lambda with map()
'map() applies function to each element'
numbers=[1,2,3,4,5,6]
result=list(map(lambda x:x*2,numbers))
print(result)

#Lambda with filter()
'filter() selects the elements satisfying the condition'
number=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2==0,number))
print(result)


