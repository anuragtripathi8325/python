# ==========================================
#         FILE HANDLING IN PYTHON
# ==========================================

# Definition:
# File Handling is used to create, open, read,
# write, and close files in Python.

# Syntax:
# file = open("file_name", "mode")

# file_name : Name of the file
# mode      : How the file will be used

# Common Modes:
# "r" = Read
# "w" = Write
# "a" = Append
# "x" = Create
# "b" = Binary
# "t" = Text (Default)

# ------------------------------------------
# Example 1 : Read a File
# ------------------------------------------

# Create a file named sample.txt
# sample.txt
# --------------------
# Hello Python
# Welcome to File Handling
# --------------------

# Open the file in read mode
file = open("sample.txt", "r")

# Read the file content
data = file.read()

# Print the content
print(data)

# Close the file
file.close()

# Output:
# Hello Python
# Welcome to File Handling

# ------------------------------------------
# Explanation
# ------------------------------------------

# open()   -> Opens the file.
# read()   -> Reads all data from the file.
# print()  -> Displays the file content.
# close()  -> Closes the file after use.

# Note:
# Keep sample.txt and this Python file
# in the same folder.

# open, read & close file
# we have to open a file before reading or writing.
# f = open("file_name", "mode")
# file_name = sample.txt  ,"mode" = r : read mode
# file_name = demo.docx   ,"mode" = w : write mode
# data = f.read()
# f.close()
# Q 1
f = open("sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
