# oop in python 
# TO map with real world scenarios , we started using objects in code.
# This is called object oriented programing (OOP)
# class & object in python 
# class is a blueprint for creating objects. 
# creating class 
# class student :
# name = "karan kumar"
# creating object (instance)
# s1 = student()
# print(s1.name)
# Q 1

class student :
    name = "karan kumar"

s1 = student()
print(s1.name)
s2 = student()
print(s2.name)

# oop in python 

# Q 2

class car:
    color = "blue"
    brand = "mercedes"
car1 = car()
print(car1.color)
print(car1.brand)


# oop in python 
# __init__ function 
# costructor
# All classes have a function called __init__ which is always executed when the class is being initiated.

# creating a class                             # creating object 

# class student:                              
#     def __init__(self, fullname):            s1 = student("karan")
#         self.fullname = fullname             print(s1.fullname)  

# * The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# Q 1

class student:
    name = "karan"
    def __init__(self):
        print("adding a new student in database..")

s1 = student()

# Q 2

class student:
    name = "karan"
    def __init__(self):
        print(self)
        print("adding a new student in database..")

s1 = student()        

# Q 4
class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")

# Q 3
class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")


s1 = student("karan")
print(s1.name)


# Q 4
class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")


s1 = student("karan")
print(s1.name)

s2 = student("anurag")
print(s2.name)

# Q 5
class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = student("Anurag", 87)
print(s1.name, s1.marks)

s2 = student("Tripathi", 89)
print(s2.name, s2.marks)

# Q 6

class student:

    #default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name,marks,):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = student("Anuarag", 88)
print(s1.name, s1.marks)

s2 = student("Akash",45)
print(s2.name,s2.marks)

# Q 7

class student:
    collage_name = "ABC College"

    #default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name,marks,):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = student("Anuarag", 88)
print(s1.name, s1.marks)

s2 = student("Akash",45)
print(s2.name,s2.marks)

print(s2.collage_name)

# Q 8

class student:
    collage_name = "ABC College"
    name = "anonymous"  # class attr

    #default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name,marks,):
        self.name = name  # obj attr > class attr
        self.marks = marks
        print("adding new student in database..")

s1 = student("Anuarag", 88)
print(s1.name, s1.marks)

s2 = student("Akash",45)
print(s2.name,s2.marks)

print(s2.collage_name)

# Q 9
class student:
    collage_name = "ABC Collage"

    def  __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student")


s1 = student("Anurag",89)
s1.welcome()

# Q 10
class student:
    collage_name = "ABC Collage"

    def  __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)


s1 = student("Anurag",89)
s1.welcome()

# Q 11
class student:
    collage_name = "ABC Collage"

    def  __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks


s1 = student("Anurag",89)
s1.welcome()
print(s1.get_marks())
