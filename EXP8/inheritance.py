# 1. Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()


# 2. Multiple Inheritance
class Father:
    def drive(self):
        print("Father drives")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):
    def play(self):
        print("Child plays")

c = Child()
c.drive()
c.cook()
c.play()


# 3. Multilevel Inheritance
class A:
    def show_a(self):
        print("A")

class B(A):
    def show_b(self):
        print("B")

class C(B):
    def show_c(self):
        print("C")

obj = C()
obj.show_a()
obj.show_b()
obj.show_c()


# 4. Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()


# 5. Hybrid Inheritance
class A:
    def show_a(self):
        print("A")

class B(A):
    def show_b(self):
        print("B")

class C(A):
    def show_c(self):
        print("C")

class D(B, C):
    def show_d(self):
        print("D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()


# 6. Public Member
class Student:
    def __init__(self):
        self.name = "Atharv"

s = Student()
print(s.name)


# 7. Protected Member
class Parent:
    def __init__(self):
        self._age = 21

class Child(Parent):
    def show(self):
        print(self._age)

c = Child()
c.show()


# 8. Private Member
class Person:
    def __init__(self):
        self.__salary = 50000

    def show_salary(self):
        print(self.__salary)

p = Person()
p.show_salary()

# print(p.__salary)     # Error


# 9. Method Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# 10. super()
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()


# 11. Constructor in Inheritance
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("Student constructor")

s = Student("Atharv", 101)

print(s.name)
print(s.roll)