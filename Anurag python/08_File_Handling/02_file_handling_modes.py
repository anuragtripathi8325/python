# ==========================================
# Python File Handling Modes (Easy Notes)
# ==========================================

# 1. 'r'  --> Read Mode
# Definition:
# Opens an existing file to read data.
# Error if file does not exist.




f = open("sample.txt", "r")
print(f.read())
f.close()


# ------------------------------------------

# 2. 'w' --> Write Mode
# Definition:
# Creates a new file if it does not exist.
# Removes all old data before writing.

f = open("sample.txt", "w")
f.write("Hello Python Anurag")
f.close()


# ------------------------------------------

# 3. 'x' --> Create Mode
# Definition:
# Creates a new file only.
# Error if file already exists.

f = open("newfile.txt", "x")
f.close()


# ------------------------------------------

# 4. 'a' --> Append Mode
# Definition:
# Adds new data at the end of the file.
# Old data is not deleted.

f = open("sample.txt", "a")
f.write("\nWelcome")
f.close()


# ------------------------------------------

# 5. 'b' --> Binary Mode
# Definition:
# Used for binary files like image, pdf, audio.

# f = open("image.jpg", "rb")
# print(f.read(10))
# f.close()


# ------------------------------------------

# 6. 't' --> Text Mode
# Definition:
# Used for text files.
# It is the default mode.

f = open("sample.txt", "rt")
print(f.read())
f.close()


# ------------------------------------------

# 7. '+' --> Update Mode
# Definition:
# Used for both Read and Write together.

f = open("sample.txt", "r+")
print(f.read())
f.write("\nPython")
f.close()

# ==========================================
# Common Mode Combinations
# ==========================================

# "rb"  -> Read Binary
# "wb"  -> Write Binary
# "ab"  -> Append Binary

# "r+"  -> Read + Write
# "w+"  -> Write + Read (Old data deleted)
# "a+"  -> Append + Read

# Reading a file 
# data = f.read()  reads entire file
# data = f.readline() reads one line at a time
# Q 1 

f = open("sample.txt", "r")

data = f.read(5)
print(data)

f.close()


# Reading a file 
# data = f.read()  reads entire file
# data = f.readline() reads one line at a time
# Q 2

f = open("sample.txt", "r")

line1 = f.readline()
print(line1)

f.close()

 # Reading a file 
# data = f.read()  reads entire file
# data = f.readline() reads one line at a time
# Q 3

f = open("sample.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
 

# Writing to a file 
# f = open("demo.txt", "w")
# f. write("this is a new line") overwrites the entire  file
# f = open("demo.txt","a")\
# f.write("this is a new line ") adds to the file 
# Q 4

f = open("sample.txt", "w")
f.write("I want to learn javascript tomorrow. 123")
f.close()

# Writing to a file 
# f = open("demo.txt", "w")
# f. write("this is a new line") overwrites the entire  file
# f = open("demo.txt","a")\
# f.write("this is a new line ") adds to the file 
# Q 5

f = open("sample.txt", "a")
f.write(" Then i will move ReactJS ")
f.close()

# Writing to a file 
# f = open("demo.txt", "w")
# f. write("this is a new line") overwrites the entire  file
# f = open("demo.txt","a")\
# f.write("this is a new line ") adds to the file 
# Q 6

f = open("sample.txt", "a")
f.write("\nAfter that nodeJS ")
f.close()

f = open("sample.txt", "r+")

f.write("it ")

f.close()

# Q 2
f = open("sample.txt", "r+")

f.write("it ")
print(f.read())
f.close()

# with syntax 
# with open("demo.txt", "a") as f:
#        data = f.read()
# Q 1

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)


# with syntax 
#ith open("demo.txt", "a") as f:
#        data = f.read()
# Q 2
with open("sample.txt", "w") as f:
    f.write("new data")

# Deleting a file 
# using the os module
# module provides a method called remove() to delete a file.
# import os
# os.remove("file.txt")
import os
os.remove("sample.txt")  # Replace "sample.txt" with the name of the file you want to delete

