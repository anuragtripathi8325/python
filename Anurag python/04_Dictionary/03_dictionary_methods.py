# Dictionary Methods 
 # (3) my Dict.items() returns all (key,val) pairs as tuples  
 # Q 9
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
pairs = list(student.items())
print(pairs[0])

 # Dictionary Methods 
 # (3) my Dict.items() returns all (key,val) pairs as tuples  
 # Q 10
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
pairs = list(student.items())
print(pairs[0])
print(pairs[1])


 # Dictionary Methods 
 # (3) my Dict..get("key") returns the key according to value  
 # Q 11
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
print(student["name"])


 # Dictionary Methods 
 # (3) my Dict.get("key") returns the key according to value 
 # Q 12
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
print(student["name"])
print(student.get("name"))


 # Dictionary Methods 
 # (3) my Dict.update(new Dict) inserts the specified items to the divctionary.
 # Q 13
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }

student.update({"city" : "delhi"})
print(student)


 # Dictionary Methods 
 # (3) my Dict.update(new Dict) inserts the specified items to the divctionary.
 # Q 14
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
new_dict = {"city" : "delhi"}
student.update(new_dict)
print(student)

 # Dictionary Methods 
 # (3) my Dict.update(new Dict) inserts the specified items to the divctionary.
 # Q 15
student = {
     "name" : "Anurag Tripathi",
     "subjects" :{
         "phy": 94.4,
         "maths" : 88.8,
         "chem" : 75.5,
     }
 }
new_dict = {"name" : "Anupam Tripathi","city" : "delhi"}
student.update(new_dict)
print(student)
