# Let's Practice 
# Q 1 
# Write a recursive function to calculate the sum of first n natural numbers .

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n 

sum = calc_sum(5)
print(sum)    

# Let's Practice 
# Q 2
# Write a recursive function to calculate the sum of first n natural numbers .

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n 

sum = calc_sum(10)
print(sum)  

# Let's Practice 
# Q 3
# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)
