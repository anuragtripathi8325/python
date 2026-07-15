# Set Methods
# set.add(el) adds an element
# Q 1 
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

# Set Methods
# set.remove(el) removes the element 
# Q 2 
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(2)

print(collection)

# Set Methods
# set.clear() empties the set  
# Q 3
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.clear()

print(len(collection))

# Set Methods
# set.pop() removes a random value 
# Q 4
collection = {"hello", "Anurag Tripathi", "learning", "python"}


print(collection.pop())

# Set Methods
# set.pop() removes a random value 
# Q 5
collection = {"hello", "Anurag Tripathi", "learning", "python"}


print(collection.pop())

# Set Methods
# set.union(set2 ) combines both set values & returns new  
# Q 6

set1 = {1,2,3,4}
set2 = {2,2,3,4}
print(set1.union(set2))

# Set Methods
# set.union(set2 ) combines both set values & returns new 
# Q 6

set1 = {1,2,3,4}
set2 = {2,2,3,4}
print(set1)
print(set2)
print(set1.union(set2))

# Set Methods
# set.intersection(set2 ) combines common values & returns new 
# Q 7

set1 = {1,2,3,4}
set2 = {2,2,3,4}
print(set1)
print(set2)
print(set1.intersection(set2))
