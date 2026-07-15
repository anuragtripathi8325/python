# let' s practice 
# (Q 1) store following word meanings in a python dictionary :
# table : " a piece of furniture ", "list of facts & figures "
# cat : "a small animal"

dictionary = {
     "cat" : "a small animal",
     "table": ["a piece of furniture","list of facts & figure"]

 }
print(dictionary)


# let' s practice 
# (Q 2) you are given  a list of subjects or students . assume one classroom is required for 1 subject.
#  how many classrooms are needed by all students.
# "python" , "java", "c++", "python", "javascript", 
# "java", "python","java", "c++", "c"


subjects= {
    "python" , "java", "c++", "python", "javascript", 
     "java", "python","java", "c++", "c"
 }
print(len(subjects))

# let' s practice 
# (Q 3) wap to enter marks of 3 subjects from the user and store them in a dictionry.
# start with an empty dictionary & add one by one use subjects name as key & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)


# let' s practice 
# (Q 4) figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built -in n data types)

values = {9, "9.0"}
print(values)

# let' s practice 
# (Q 5) figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built -in n data types)

values = {
    ("float", 9.0),
    ("int",9)
}

print(values)

