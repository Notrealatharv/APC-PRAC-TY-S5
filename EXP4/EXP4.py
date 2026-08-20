'Q1)'
import time
student=[]
grades=[]

def addlist(stu,grd):
    student.append(stu)
    grades.append(grd)

def update(stu,grd):
    if stu in student:
        indexs=student.index(stu)
        grades[indexs]=grd
    else:
        print("student not found")

def dele(stu):
    if stu in student:
        indexs=student.index(stu)
        student.pop(indexs)
        grades.pop(indexs)
    else:
        print("student not found")
def avaragegrd():
    if len(grades)>0:
        print("avarage",sum(grades)/len(grades))
    else:
        print("list empty")

def extream():
    if len(grades)>0:
        print("max grades are:",max(grades))
        print("min grades are:",min(grades))


addlist("atharv",23)
addlist("devang",2)
addlist("harsh",23)
addlist("kate",54)
addlist("soham",23)
print(student,grades)
time.sleep(2)
update("atharv",12) 
print(student,grades)
time.sleep(2)
dele("atharv")
print(student,grades)
avaragegrd()
extream()
