 # Let ' s practice 
# Q 1 
# create a new file "practice.txt" usimg python. Add the following in it.
# Hi everyone
# we are learning file i/O
# Using java.
# i like programming in java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning file i/O\n")
    f.write("Using java.\n")
    f.write("i like programming in java.\n")

# Let ' s practice 
# Q 2  
# WAF that replace all occurrences of "java" with "python" in above file.
# search if the word "learning" exists in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()


new_data = data.replace("java", "python")
print(new_data)

# Let ' s practice 
# Q 3
# WAF that replace all occurrences of "java" with "python" in above file.
# search if the word "learning" exists in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()


new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
# Let ' s practice 
# Q 4
# WAF that replace all occurrences of "java" with "python" in above file.
# search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("not found")    
# Let ' s practice 
# Q 5
# WAF that replace all occurrences of "java" with "python" in above file.
# search if the word "learning" exists in the file or not.

word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("not found")    

# Let ' s practice 
# Q 6
# WAF that replace all occurrences of "java" with "python" in above file.
# search if the word "learning" exists in the file or not.

def check_for_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
             print("Found")
        else:
            print("not found")
check_for_word()               

# Let ' s practice 
# Q 6
# WAF to find in which line of the file does the word "learning" occur first
# print - 1 if word not found

def check_for_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())        
 
# Let ' s practice 
# Q 7
# WAF to find in which line of the file does the word "learning" occur first
# print - 1 if word not found

def check_for_line():
    word = "python"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())        
 

 # Let ' s practice 
# Q 8
# from a file containing numberas separated by comma, print the count of even numbers 

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = " "
    for i in range(len(data)):
        if (data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

# Let ' s practice 
# Q 9
# from a file containing numberas separated by comma, print the count of even numbers 

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for value in nums:
        if int(value) % 2 == 0:
            count += 1

print(count)
