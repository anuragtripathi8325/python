# function in python
# Block of statement that perform a specific task.
# def func_name(param 1, param 2..):   
# some work 
# return val
# func_name(arg1 ,arg2..) function cal

def calc_sum(a,b):
     sum = a + b
     print(sum)
     return sum

# function calls

calc_sum(5,10)

# more line of code
 
calc_sum(2,10)

# more lines of code

calc_sum(12,17)

# function in python
# Block of statement that perform a specific task.
# def func_name(param 1, param 2..):   
# some work 
# return val
# func_name(arg1 ,arg2..) function call
# Q 2

def calc_sum(a,b):
    return a + b

sum = calc_sum(166,133)
print(sum)

# Function definition

def calc_sum(a,b): #parameters
    return a + b

sum = calc_sum(16366,14533) #function call ; arguments
print(sum)


# average of 3 numbers 

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(98,97,95)

# Default Parameters
# Assigning a default value to parameter, Which is used when no argument is passed
# Q 5

def cal_prod(a = 4, b = 2):
    print(a * b)
    return a * b

cal_prod()  
