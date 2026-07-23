# Let's practice 
# Q 1
# WAF to print the length of a list.(list is the parameter)
cities = ["delhi", "gurgoan","noida", "pune","banglore","mumbai",]
heroes = ["sunny","srk","salman","king","ajay","ranver","prabhsh",]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)  

# Let's practice 
# Q 2
# WAF to print the elements of a list in a single line.(list is the parameter)

cities = ["delhi", "gurgoan","noida", "pune","banglore","mumbai",]
heroes = ["sunny","srk","salman","king","ajay","ranver","prabhsh",]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print()
print_list(heroes)
print()    

# Let's practice 
# Q 3
# WAF to find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)  
  
# Let's practice 
# Q 4
# WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "usd =", inr_val, "INR")

converter(1)       

# Let's practice 
# Q 5
# WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "usd =", inr_val, "INR")

converter(73)       
