#file handling


'creating a file:'
# file=open("exp6.txt","x")
# file.colse()


'write:'
# file=open("exp6.txt","w")
'using write:'
# file.write("hello python")
# file.write(",hello world\n")

'using writelines'
# lines=["how ","are ","you"]
# file.writelines(lines)
# file.close()

'APPEND:USED TO WRITE WITHOUT ERASING'
# file=open("exp6.txt","a")
# file.write("\ni am atharv")

'reading whole file'
# file = open("exp6.txt", "r")
# data = file.read()
# print(data)
# file.close()

'one line read'
# file=open("exp6.txt","r")
# data=file.readline()
# print(data)
# file.close()

'readlines functon'
# file=open("exp6.txt","r")
# data=file.readlines()
# print(data)
# file.close()

'read using a for loop'
# file=open("exp6.txt","r")
# for lines in file:
#     print(lines)
# file.close()

'read and write using r+'
# file=open("exp6.txt","r+")
# print(file.read())
# file.write("hello")
# file.close()

'write and read :deletes old content first'
# file=open("exp6.txt","w+")
# file.write("all cleared first")
# print(file.read())

'append and read a+'
# file=open("exp6.txt","a+")
# file.write("\nappend success")
# file.seek(0)    #used to make the cursor come at first
# print(file.read())

'WITH OPEN : USED TO AUTOMATICALLY CLOSE FILE'
# with open ("exp6.txt") as file:
#     print(file.read())

'tell function'
# file = open("exp6.txt", "r")
# print(file.tell())
# print(file.read(5))
# print(file.tell())
# file.close()

'os function'
# import os
# if os.path.exists("exp6.txt"):
#     print("file exists")
# else:
#     print("file DNE")

'delete file'
# import os
# import time
# file=open("trash.txt","x")
# file.close()
# time.sleep(5)
# os.remove("trash.txt")

'rename'
# import os
# import time
# file=open("name.txt","x")
# file.close()
# time.sleep(3)
# os.rename("name.txt","rename.txt")
# time.sleep(3)
# os.remove("rename.txt")


'binary read write'
# file=open("binary.bin","x")
# file.close()
# file=open("binary.bin","wb")
# data = b"Hello Python"
# file.write(data)
# file.close()

'read binary'
# file = open("binary.bin", "rb")
# data = file.read()
# print(data)
# file.close()

'append binary'
# file = open("binary.bin", "ab")
# file.write(b"Hello")
# file.close()

'image read write'
# file1=open("download.jpg","rb")
# # print(file1.read())
# file2=open("copy.jpg","wb")
# for data in file1:
#     file2.write(data)
# file1.close()
# file2.close()

############################################################
#############################################################
'Directory Handling'
# import os

# Create a directory
# os.mkdir("students")

# Check if directory exists
# if os.path.exists("students"):
#     print("Directory exists")
# else:
#     print("Directory does not exist")


# Create Multiple Directories

# os.makedirs("college/cse/students")
# print("Directories created successfully")