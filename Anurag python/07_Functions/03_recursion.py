# Recursion
# When a function calls itself repeatedly.
# prints n to 1 backwards
# def show(n):
#   if(n == 0):
#      return
#   print(n)
#   show(n-1)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

# Recursion
# When a function calls itself repeatedly.
# prints n to 1 backwards
# def show(n):
#   if(n == 0):
#      return
#   print(n)
#   show(n-1)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(5)    

# Recursion
# When a function calls itself repeatedly.
# prints n to 1 backwards
# def show(n):
#   if(n == 0):
#      return
#   print(n)
#   show(n-1)
# Q 2

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(2))         

# Recursion
# When a function calls itself repeatedly.
# prints n to 1 backwards
# def show(n):
#   if(n == 0):
#      return
#   print(n)
#   show(n-1)
# Q 3

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(4))         

# Recursion
# When a function calls itself repeatedly.
# prints n to 1 backwards
# def show(n):
#   if(n == 0):
#      return
#   print(n)
#   show(n-1)
# Q 4

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(10))         
