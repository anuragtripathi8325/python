# let 's practice 
# Q 1 create student class  that takes name $ marks of 3 subjects as arguments in constructor 
# Then create a method to print the average 

class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks 

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is :", sum/3)

s1 = student("tony stark",[99,98,97])
s1.get_avg()

# Q 2 
class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks 

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is :", sum/3)

s1 = student("tony stark",[99,98,97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()


# Q 3
# Create Account class with 2 attributes - balance & account no.
# create method for debit, credut & printing the balance. 

class Account:
    def __init__(self, bal, acc):
        self.balnce = bal
        self.account_no = acc

acc1 = Account(10000, 12345)
print(acc1.balnce)
print(acc1.account_no)        


# Q 4
# Create Account class with 2 attributes - balance & account no.
# create method for debit, credut & printing the balance. 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

# complex number 
# Q 5
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

num1 = complex(1, 3)
num1.showNumber()

  
# Q 6
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

# complex number 
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)

num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()
# complex number
# Q 7
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img, "j")

    def __sub__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
            newReal = self.real - num2.real
            newImg = self.img - num2.img
            return Complex(newReal, newImg)
    

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 - (num2)
num3.showNumber()

 
# Q 8  Define a circle to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius 

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# Define a Employee class with attributes role, department & salary. 
# This class show Details() method.
# Create an Engineer class that inherits properties from Employee & attributes : name & age.
# Q 9 
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role 
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()            

# Define a Employee class with attributes role, department & salary. 
# This class show Details() method.
# Create an Engineer class that inherits properties from Employee & attributes : name & age.
# Q 10
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role 
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")        

engg1 = Engineer("Elon musk", 40)
engg1.showDetails()

#  Q 11 
# Create a clss called order which stores item & its price.
# use Dunder function _ _gt _ _() to convey that:
# order1> order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price 

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)

