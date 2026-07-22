# let 's practice
# Q1  print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1

# let 's practice
# Q 2  print numbers from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1
 
# let 's practice
# Q 3  print the multiplication table of a number n. 

i = 1
while i <= 10:
    print(3*i)
    i += 1

   
# let 's practice
# Q 3  print the multiplication table of a number n. 

n = (int(input("enter number : ")))
i = 1
while i <= 10:
    print(n*i)
    i += 1
 

# let 's practice
# Q 4  print the  elements of thee following list using a loop . 
nums = [1,4,9,16,25,36,49,64,81,100 ]
idx = 0
while idx <len(nums) :
    print(nums[idx])
    idx +=1


 # let 's practice
# Q 5 search for a number x in this tuple using loop. 


nums = [1,4,9,16,25,36,49,64,81,100]

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("FOUND at idx", i)
    else:
        print("finding..")
    i += 1


 # let 's practice
# break and continue 
 
i = 0
while i <= 5:
    if(i ==3):
        i +=1
        break
    print(i)
    i +=1


 # let 's practice
# break and continue 
 
i = 0
while i <= 5:
    if(i ==3):
        i +=1
        continue
    print(i)
    i +=1
