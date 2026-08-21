# Guess the number
# Q 1

import random 
randNum = random.randint(1,5)
print(randNum)
# Q 2

import random 

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the traget  : "))
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number wass too small. Take a bigger guess ...")
    else:
        print("your number wass too big. Take a smaller guess...")
print("-----GAME OVER----")        

# Guess the number
# Q 3

import random 

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the traget or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number wass too small. Take a bigger guess ...")
    else:
        print("your number wass too big. Take a smaller guess...")


print("-----GAME OVER----")        
