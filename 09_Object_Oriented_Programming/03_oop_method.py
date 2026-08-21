# super method 
# super() method is used to acess method of the parent class.
# Q 1 
class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = Toyotacar("prius", "electric")
print(car1.type)

# Q 2
class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = Toyotacar("prius", "electric")
print(car1.type)


# class method
# A class method is bound to the class & receive the class as an implict first argument.
# Note- static method can't access or modify class state & generally for utility.
# class student:
# @classmethod  # decorator
# def college(cls):
#   pass
# Q 1

class person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = person()
p1.changeName("Anurag Tripathi")
print(p1.name)

# Q 2

class person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = person()
p1.changeName("Anurag Tripathi")
print(p1.name)
print(person.name)

# Q 3

class person:
    name = "anonymous"

    def changeName(self, name):
        person.name = name

p1 = person()
p1.changeName("Anurag Tripathi")
print(p1.name)
print(person.name)

# Q 4

class person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Anurag"

p1 = person()
p1.changeName("Anurag Tripathi")
print(p1.name)
print(person.name)

# Q 4

class person:
    name = "anonymous"

   # def changeName(self, name):
    #    self.__class__.name = "Anurag"
     
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = person()
p1.changeName("Anurag Tripathi")
print(p1.name)
print(person.name)  

# Property
# We use @property decorator on any method in the class to use the method as a property
# Q 1 

class student:
    def __init__(self, phy ,chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98 ,97, 99)
print(stu1.percentage)

# Q 2

class student:
    def __init__(self, phy ,chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98 ,97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)

# Q 3

class student:
    def __init__(self, phy ,chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"   

stu1 = student(98 ,97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)

# Polymorphism : operator overloading
# when the same operator is allowed to have different meaning according to the context>
# operators & Dunder functions
# a+b addition         a.__add__(b)
# a-b subtraction     a__sub__(b)
# a*b  multiplication    a__mul ___(b)
# a/b  divison        a__truediv__(b)
# a % b addition       a__mod ___(b)

print(1 + 2)
print(type(1))
print("apna" +"college") # concatenate
print([1, 2, 3] +[4, 5, 6]) #merge
