# n=int(input("enter nth element : "))
# python program to print numbers upto n
# for i in range (0,n):
    # print(i)

#even numbers up to n
# for i in range(0,n,2):
#     print(i)

# print odd numbers
# for i in range(0,n):
#      if(i%2!=0):
#         print(i)

# print n2
# for i in range(1,n):
#     print(i**2)

# sum of 1 by nfactorial 
# sum=1
# import math

# for i in range(1,n):
#     sum=sum+1/math.factorial(i)
# print(sum)    

#  abc abc abc
# for i in range (1,4):
#     for i in range(65,67):
#         print(chr(i),end="")
#     print()

#design\
# n=int(input("n= "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(chr(65+j),end=" ")
#     print()    

# design2
# n=int(input("n="))
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(chr(65+j),end=" ")
#     print()

# design\
# n=int(input("n="))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# design
# n=int(input("n="))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#########################################

#whileloop
# i=0
# while(i!=10):
#     print(i)
#     i=i+1

#even
# i=0
# while(i!=10):
#     print(i)
#     i=i+2

# odd
# n=int(input("n="))
# i=0
# while(i!=n):
#     if(i%2!=0):
#         print(i)
#     i=i+1 
    
# sum of 1 to n
# n=int(input("n="))
# i=1
# sum=0
# while(i!=n+1):
#     sum=sum+i
#     i=i+1
# print(sum)

# sum of odd num

# n=int(input("n="))
# i=0
# sum=0
# while(i!=n):
#     if(i%2!=0):
#         sum=sum+i
#     i=i+1 
# print(sum)

# sum of even num

# n=int(input("n="))
# i=0
# sum=0
# while(i!=n+1):
#     if(i%2==0):
#         sum=sum+i
#     i=i+1 
# print(sum)

# reverse
# n=int(input("n="))
# i=10
# while(i!=0):
#     print(i)
#     i=i-1

n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1