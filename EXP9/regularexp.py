#REGEX 
import re
# 1 re.compile() , compile() creates regex pattern and pattern can be reused 

pattern =re.compile(r"\d+")
text="i have 20 appels and 34 bananas"

print(pattern)


# 2. re.search()
# search() finds the FIRST occurrence of the pattern
# Returns a match object if found

pattern=re.compile(r"\d+")
text="i have 20 appels and 34 bananas"
result=pattern.search(text)
if result:
    print(result.group())
else:
    print("not found")

# 3. re.findall()
# findall() finds ALL occurrences
# Returns a list

pattern = re.compile(r"\d+")
text = "I have 25 apples and 10 bananas"
result = pattern.findall(text)
print("All numbers:", result)

# 4. re.match()
# match() checks only at the BEGINNING of the string

pattern = re.compile(r"Hello")

text = "Hello Atharv"

result = pattern.match(text)

if result:
    print("Matched:", result.group())
else:
    print("No match")

# 5. re.fullmatch()
# fullmatch() checks whether the ENTIRE string matches  

pattern=re.compile(r"hello Atharv")
text="hello Atharv"
result=pattern.fullmatch(text)
if result:
    print("found:",result.group())
else:
    print("NO MATCH")

# 6. re.finditer()
# finditer() returns match objects for ALL occurrences

pattern = re.compile(r"\d+")

text = "Age 20, Roll 101, Marks 95"

for match in pattern.finditer(text):
    print("Found:", match.group())
    print("Position:", match.start(), "-", match.end())

# 7. EMAIL VALIDATION

text = "Contact me at atharv@gmail.com"
pattern = r"[\w.-]+@[\w.-]+\.\w+"
result = re.findall(pattern, text)
print("Email:", result)

#8. PHONE NUMBER

text = "Call me at 9876543210"
pattern = r"\d{10}"
result = re.findall(pattern, text)
print("Phone:", result)

# 9. password validator

password = input("Enter password: ")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$"
result = re.fullmatch(pattern, password)

if result:
    print("Valid Password")
else:
    print("Invalid Password")