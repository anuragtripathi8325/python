# Q 1list 
marks = [94.4,84,5,45.6,55,5,88.6]
print (marks)

#  Q 2 list 
marks = [94.4,84,5,45.6,55,5,88.6]
print (marks)
print(type(marks))
 
 # Q 3 list 
marks = [94.4,84,5,45.6,55,5,88.6]
print(marks[0])
print(marks[1])
 
#Q 4 list 
marks = [94.4,84,5,45.6,55,5,88.6]
print(marks[0])
print(marks[1])
print(len(marks))

 # Q 4 list 
student =["Anurag tripathi",95.4,"East Delhi"]
print(student)

# tuple
# Q 1
tup = (1,2,3,4)
print(type(tup))


# tuple
# Q 2
tup = (1,2,3,4)
print(tup[0])
print(tup[2])

# let ' s practice 
#  Q 5 wap to ask the user to enter names of their 3 favorite movvies & store them in a list 

movies  = []
mov1 = input("Enter 1st movie ")
mov2 = input("Enter 2nd movie ")
mov3 = input("Enter 3rd movie ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# let ' s practice 
# Q 6 wap to ask the user to enter names of their 3 favorite movvies & store them in a list 

movies  = []
mov1 = input("Enter 1st movie ")
movies.append(mov1)
mov2 = input("Enter 2nd movie ")
movies.append(mov2)
mov3 = input("Enter 3rd movie ")
movies.append(mov3)

print(movies)

# let ' s practice 
# Q 7 wap to ask the user to enter names of their 3 favorite movvies & store them in a list 

movies  = []
movies.append(input("Enter 1st movie "))
movies.append(input("Enter 2nd movie "))
movies.append(input("Enter 3rd movie "))
print(movies)

# let ' s practice 
# Q 8 wap to check if a list contains a palindrome of elements .(Hint:usecopy()methood)

list1 = [1,2,1]
list2 =[1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")    

# let ' s practice 
# Q 9 wap to check if a list contains a palindrome of elements .(Hint:usecopy()methood)

list1 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")    

# let ' s practice 
# Q 10 wap to check if a list contains a palindrome of elements .(Hint:usecopy()methood)

list1 = ["m","a","a","m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")    

# let ' s practice 
# Q 11 wap to check if a list contains a palindrome of elements .(Hint:usecopy()methood)

list1 = ["m","a","a","m", "a"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")    

# let ' s practice 
# Q 12 wap to count the number of students with the "A" grade in the following tupple.

grade = ("C","A","A","D", "B")
print(grade.count("A")) 

# let ' s practice 
# Q 13 wap to count the number of students with the "A" grade in the following tupple.

grade = ("C","A","A","D", "B")
print(grade.count("B"))

# let ' s practice 
# Q 14  store the above values in alist & sort them from"A" to "D".

grade = ["C","D","A","A","B", "B","A"]
grade.sort()
print(grade)
