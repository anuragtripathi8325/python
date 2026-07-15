# list slicing :- simiar to string slicing 
# list_name[starting_idx:ending_idx]ending index is not included

marks = [94 ,55, 66, 77, 88, 45, 76]
print(marks[1:4])

# Q 2 list slicing :- simiar to string slicing 
# list_name[starting_idx:ending_idx]ending index is not included

marks = [94 ,55, 66, 77, 88, 45, 76]
print(marks[0:4])

# Q 3 list slicing :- simiar to string slicing 
# list_name[starting_idx:ending_idx]ending index is not included

marks = [94 ,55, 66, 77, 88, 45, 76]
print(marks[0:])

# Q 4 list slicing :- simiar to string slicing 
# list_name[starting_idx:ending_idx]ending index is not included

marks = [94 ,55, 66, 77, 88, 45, 76]
print(marks[-3:-1])


# list method 
# list.append(4) adds one element at the end 
# Q 1
list =[1,2,3]
list.append(4)
print(list)

# list method 
#list.sort() sorts in ascending order [1,2,3]
# Q 2 
list =[2,1,3]
print(list.append(4))
print(list.sort())
print(list)

# list method 
#list.sort() sorts in ascending order [1,2,3]
# Q 3
list =[2,1,3,6,5,4]
print(list.sort())
print(list)

# list method 
#list.sort(reverse = True) sorts in descending order [3,2,1]
#Q4
list =[2,1,3,6,5,4]
print(list.sort(reverse=True))
print(list)


# list method 
#list.sort(reverse = True) sorts in descending order [3,2,1]
# Q 5 
list =["banana", "litchi","apple"]
print(list.sort(reverse = True))
print(list)


# list method 
#list.sort(reverse = True) sorts in descending order [3,2,1]
# Q 6
list =["banana", "litchi","apple"]
print(list.sort())
print(list)

# list method 
#list.sort(reverse = True) sorts in descending order [3,2,1]
# Q 7 
list =["b","c","e","g","d","a","k","f","l","j","h","i",]
print (list.sort())
print(list)

# list method 
#list.sort(reverse = True) sorts in descending order [3,2,1]
# Q 8 
list =["b","c","e","g","d","a","k","f","l","j","h","i",]
print (list.sort(reverse = True))
print(list)

# list method 
#list.reverse()Reverse list 
# Q 9 
list =["b","c","e","g","d","a","k","f","l","j","h","i",]
print (list.reverse())
print(list)

# list method 
#list.insert(idx, el)insert element at index 
# Q 10 
list =[2,1,3]
list.insert(1,5)
print(list)

# list method 
#list.remove(1) remove first occurrence of element 
# Q 11 
list =[2,1,3]
list.remove(1)
print(list)

# list method 
#list.pop(idx) remove element at idx 
# Q 12 
list =[2,1,3]
list.pop(2)
print(list)
 
 # tuple slicing 
tup = [1,2,3,4]
print(tup[1:3])

# tuple method 
# tup.index (el) returns index of first occurrence tup.index(1)is 1
# Q 3 
tup = [1,2,3,4]
print(tup.index(3))

 
# tuple method 
# tup.count (el) counts total  occurrence tup.count(1)is 2
# Q 4
tup = [1,2,3,4]
print(tup.count(3))

# tuple method 
# tup.count (el) counts total  occurrence tup.count(1)is 2
# Q 5
tup = [1,2,3,2 ,2]
print(tup.count(2))


