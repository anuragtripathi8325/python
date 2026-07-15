# dict 
# Q 1
info = {
    "key": "value",
    "name": "Anurag Tripathi",
    "learning" :"python",
    "from" : "Apna collage",
}
print(info)

# dict 
# Q 2 
info = {
    "age" : 22,
    "its_adult" :True,
    "marks": 94.4,
}
print(info)

# dict 
# Q 3 
info = {
    "age" : 22,
    "its_adult" :True,
    "marks": 94.4,
}
print(type(info))

# dict 
# Q 4 
info = {
    "key": "value",
    "name": "Anurag Tripathi",
    "topics": "dict_set",
    "learning" :"python",
    "from" : "Apna collage",
    "age" : 22,
    "its_adult" :True,
    "marks": 94.4,
}

print(info["name"])
print(info["age"])
print(info["topics"])
print(info["learning"])


# dict 
# dictionary value change 
# Q 5 
info = {
    "key": "value",
    "name": "Anupam Tripathi",
    "topics": "dict_set",
    "learning" :"python",
    "from" : "Apna collage",
    "age" : 22,
    "its_adult" :True,
    "marks": 94.4,
}
# dictionary value change 

info["name"] = "Anurag"
info["surname"] = "Tripathi"
print(info)

# empty dict
# Q 6

null_dict = {}
print(null_dict)

 # nested dictionary 
 # Q 7 
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
print(student)

 # nested dictionary 
 # Q 8
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
print(student["subjects"])

 # nested dictionary 
 # Q 9
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
print(student["subjects"]["maths"])
