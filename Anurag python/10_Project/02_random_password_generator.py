# Random password Generator
# Q 1 
import random

val = random.choice([1, 2, 3])
print(val)

# Random password Generator
# Q 2 
import random

val = random.choice(['a', 'b', 'c', 'd',])
print(val)

# Random password Generator
# Q 2 
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password =""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is :", password)    

# Q 3
import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

password =""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is :", password)    

# Q 4
import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

res = [random.choice(charValues) for i in range(pass_len)]
print(res)

# Random password Generator
# Q 5
import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

res = "X".join([random.choice(charValues) for i in range(pass_len)])
print(res)

# Random password Generator
# Q 6
import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

res = "*".join([random.choice(charValues) for i in range(pass_len)])
print(res)

# Random password Generator
# Q 7
import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation


password = "*".join([random.choice(charValues) for i in range(pass_len)])
print("your random password is:", password)
