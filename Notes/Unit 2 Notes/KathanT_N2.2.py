
## If statements

a = 1
b = 2

## Colon (:) endes if statement
if b > a:     ## If, b > a, then run the line below
    print(b, " is greater than ", a)     ## Then is begun by indenting the following line from the if statement (press TAB)


temperature = 85

if temperature > 80:
    print("It is hot outside!")     ## Prints only if the temperature is above 80

print("Have a nice day!")     ## Prints no matter what


age = 20
if age >= 18:
    print("You are an adult.")     ## There can be multiple items in an if statement
    print("You can vote.")
    print("You have full legal rights.")
    print("You can gamble.")


password = input("Enter the password: ")

if password == "1234":
    print("Access Granted")
else:
    print("Access Denied")


## If, Else

import random

flip = random.choice(["heads", "tails"])
if flip == "heads":
    print("Your coin flipped heads!")
if flip == "tails":
    print("Your coin flipped tails!")

import random

total_rolls = int(input("How many rolls would you like to simulate?\n"))
total_rolls_completed = 0
even_rolls = 0
odd_rolls = 0

while total_rolls_completed < total_rolls:
    dice_roll = random.choice([1 , 2 , 3 , 4 , 5 , 6])

    if dice_roll % 2 == 0:
        even_rolls += 1

    elif dice_roll % 2 == 1:
        odd_rolls += 1

    else:
        print ("An error has occured.")
        exit()

    total_rolls_completed += 1

print(f"There were a total of {even_rolls} even rolls and {odd_rolls} odd rolls.")
