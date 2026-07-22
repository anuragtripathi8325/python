# Let ' practice
# Q 1 
# using for 
# print the elements of the followng list using a loop :
# [1,4,9,16,25,36,49,81,100]
# search for a number x in thsi tuple using loop : 
# [1,4,9,16,25,36,49,81,100]

nums =[1,4,9,16,25,36,49,81,100]
x = 49

idx = 0 
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        break
    idx +=1

# Let ' practice
# Q 2 
# using for 
# print the elements of the followng list using a loop :
# [1,4,9,16,25,36,49,81,100]
# search for a number x in thsi tuple using loop : 
# [1,4,9,16,25,36,49,81,100]

nums =[1,4,9,16,25,36,49,81,100,49]
x = 49

idx = 0 
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        
    idx +=1


# Let' s practice
# Q 3 print numbers from 1 to 100.
# range()
# range(satrt?, stop, step?)


for i in range(1,101,): # (start,stop ,step)
    print(i)

# Let' s practice
# Q 4 print numbers from 100 to 1.
# range()
# range(satrt?, stop, step?)


for i in range(100,0, -1): # (start,stop ,step)
    print(i)

# Let' s practice
# Q 5 print the multiplication table of a  number n. 
# range()
# range(satrt?, stop, step?)

n = int(input("enter number :"))

for i in range(1,11 ): # (start,stop ,step)
    print(n*i)

# Let's practice 
# Q 6 WAP to find the sum of first n n umbers .(using while)

n = 7
sum = 0

for i in range(1, n + 1):
    sum += i

print("Total sum =", sum)

# Let's practice 
# Q 7 WAP to find the  factorial of first n numbers. (using for)

n = 7
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =" ,fact)



