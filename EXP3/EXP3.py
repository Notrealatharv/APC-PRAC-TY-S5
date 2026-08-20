# ● Write a program to input a string and display its length without using the len() function. 
# string1=input("enter the string: ")
# length=0
# for i in string1:
#     length=length+1
# print(length)

# ●	Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
# string1=input("enter the string: ")
# vowels=0
# conse=0
# space=0
# num=0
# numbers=list("1234567890")
# spec=("~!@#$%^&*")
# specc=0
# for i in string1:
#     if (i=='a' or i=='A'or i=='e'or i=='E' or i== 'I'or i=='i' or i=='O' or i=='o' or i=='u' or i=='U' ):
#         vowels=vowels+1
#     elif(i==' '):
#         space=space+1
#     elif(i in numbers):
#         num=num+1
#     elif(i in spec):
#         specc=specc+1
#     else:
#         conse=conse+1

# print("THE VOWELS ARE:",vowels)
# print("THE CONSONENTS ARE:",conse)
# print("THE SPACES ARE:",space)
# print("THE DIGITS ARE:",num)

# ●	Reverse the given string without using built-in reverse functions. 
# string1=input("ENTER STRING: ")
# for i in  string1[::-1]:
#     print(i,end='')

# ●	Check whether the entered string is a palindrome. 
# string1=input("ENTER STRING: ")
# if(string1==string1[::-1]):
#     print("IS A PALINDROME")
# else:
#     print("IS NOT A PALINDROME")


# ●	Count the number of uppercase and lowercase letters in a string. 
# string1=input("ENTER STRING: ")
# low=0
# upp=0
# for i in string1:
#     if (i.islower()):
#         low=low+1
#     else:
#         upp=upp+1
# print(low)
# print(upp)


# ●	Replace all occurrences of a given character with another character. 
# string1=input("ENTER STRING: ")
# rep=string1.replace('A','X')
# print(rep)

# ●	Remove all spaces from the input string. 
# string1=input("ENTER STRING: ")
# rep=string1.replace(' ','')
# print(rep)


# ●	Find the number of times a specified character appears in a string. 
# string1=input("ENTER STRING: ")
# coun=string1.count('a')
# print(coun)

# ●	Print the first and last character of a string. 
# string1=input("ENTER STRING: ")
# print(string1[0])
# print(string1[-1])

# ●	Display each character of a string along with its ASCII value.
# string1=input("ENTER STRING: ")
# for i in string1:
#     print(i,":",ord(i),end=',')

# a.	Count the total number of words in a sentence. 
# string1=input("ENTER STRING: ")
# spc=string1.count(' ')
# print("WORDS ARE :",spc+1)

# a.	Find the longest word in a given sentence. 
# sentence=input("ENTER SENTENCE: ")
# words = sentence.split()
# longest_word = max(words, key=len)
# print("Longest word:", longest_word)

# a.	Find the shortest word in a sentence. 
# sentence=input("ENTER SENTENCE: ")
# words = sentence.split()
# shortest_word = min(words, key=len)
# print("shortest word:", shortest_word)


# a.	Convert the first letter of every word to uppercase. 
# sentence=input("ENTER SENTENCE: ")
# words = sentence.split()
# for i in words:
#     print(i.title(),end=' ')


# a.	Print all duplicate characters in a string. 




# a.	Display the frequency of every character in a string. 







# a.	Check whether two strings are anagrams. 
# string1=input("ENTER STRING1: ")
# string2=input("ENTER STRING2: ")

# clean1 = string1.replace(" ", "").lower()
# clean2 = string2.replace(" ", "").lower()

# if sorted(clean1) == sorted(clean2):
#     print("IS AN ANAGRAM")
# else:
#     print("NOT ANAGRAM")


# a.	Remove duplicate characters while maintaining the original order. 
# string1=input("ENTER STRING: ")
# result=""
# for i in string1:
#     if (i not in result):
#         result=result+i
# print(result)

# a.	Check whether a given substring exists in the main string. 
# string1=input("ENTER STRING1: ")
# string2=input("ENTER STRING2: ")

# if string1 in string2:
#     print("exist")
# else:
#     print("not exist")

# a.	Count how many times a specific word appears in a sentence. 
# string1=input("ENTER STRING: ")
# word=input("word: ")
# words=string1.split()
# count=0
# for i in words:
#     if word ==i:
#         count=count+1
# print("THE COUNT IS :",count)


# ●	Validate a password based on these conditions: 
# o	Minimum 8 characters 
# o	At least one uppercase letter 
# o	One lowercase letter 
# o	One digit 
# o	One special character

# count=0
# spec=("~!@#$%^&*")
# string1=input("ENTER STRING: ")
# if(len(string1)<8):
#     print("INVALID")
#     raise SystemExit
# for i in  string1:
#     if i.islower():
#         count=count+1
#     if i.isupper():
#         count=count+1
#     if i.isdigit():
#         count=count+1
#     if (i in spec):
#         count=count+1
#     if(count==4):
#         print("valid")
#     else:
#         print("not vlaid")



