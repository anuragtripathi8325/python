# static method 
# methods that don't use the self parameter (work at class level)
# class student:
# @staticmethod  # decorator 
# def collage():
#   print("Abc collage")
# Decorators allow us to wrap another function in order to extend the behavioiur of the
# wrapped function , without permanently modifying it 

class student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = student("tony stark" , [99,98,97])
s1.get_avg()
s1.hello()

# Abstraction
# Hiding the implementation details of a class and only showing 
# the essential features to the user.
# Q 1
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()

# del keyword 
# used to delete object properties or object itself.
# del s1.name
# del s1 

class student:
    def __init__(self, name):
        self.name = name
s1 = student("Anurag")
print(s1.name)
#del s1.name
#print(s1.name)      

# privite(like) attributes & methods 
# conceptual implementations in python 
# private attributes & methods are meant to be used only within the class
#  and are not accessible from outsid the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.acc_pass)

# inheritance 
# when one class(child/derived) derives the properties & methods of another class(parent/base).
# class car:
# .......
# class Toyotacar(car):

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.name)

# inheritance 
# when one class(child/derived) derives the properties & methods of another class(parent/base).
# class car:
# .......
# class Toyotacar(car):
# Q 2

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())

# inheritance 
# when one class(child/derived) derives the properties & methods of another class(parent/base).
# class car:
# .......
# class Toyotacar(car):
# Q 3

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.color)

#Inheritance in Python

#Inheritance:
#Inheritance means one class gets the properties and methods of another class.

#1. Single Inheritance

#When one child class inherits from one parent class, it is called Single Inheritance.

#Example:
#Parent → Child

#2. Multilevel Inheritance

#When a class inherits from another class, and another class inherits from that child class, it is called Multilevel Inheritance.

#Example:
#Grandparent → Parent → Child

#3. Multiple Inheritance

#When one child class inherits from more than one parent class, it is called Multiple Inheritance.

#Example:
#Parent1 + Parent2 → Child
# Q 1
class car:
    @staticmethod
    def start():
        print("car started..")

        @staticmethod
        def stop():
            print("car stoped.")

class ToyotaCar(car):
    def __init__(self, brand):
        self.brand = brand 

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("disel")
car1.start()  

# Q 2

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class c(A, B):
    varc = "welcome to class c"

c1 = c()

print(c1.varc)
print(c1.varB)
print(c1.varA)
