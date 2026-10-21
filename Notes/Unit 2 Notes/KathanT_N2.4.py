## Nested Conditionals

username_exists = True
password_correct = True

if username_exists:                                             ## If this is true, then do what is in the next indented part of the code
    if password_correct:                                        ## If the password is correct, then do this.
        print("Login successful! Welcome to your dashboard.")
    else:
        print("Incorrect Password. Please try again.")
else:
    print("Username not found. Please sign up.")
##############################################################################################################################
username_exists = True
password_correct = False

if username_exists:                                             ## If this is true, then do what is in the next indented part of the code
    if password_correct:                                        ## If the password is correct, then do this.
        print("Login successful! Welcome to your dashboard.")
    else:
        print("Incorrect Password. Please try again.")
else:
    print("Username not found. Please sign up.")
##############################################################################################################################
username_exists = False
password_correct = True

if username_exists:                                             ## If this is true, then do what is in the next indented part of the code
    if password_correct:                                        ## If the password is correct, then do this.
        print("Login successful! Welcome to your dashboard.")
    else:
        print("Incorrect Password. Please try again.")
else:
    print("Username not found. Please sign up.")
##############################################################################################################################
username_exists = False
password_correct = False

if username_exists:                                             ## If this is true, then do what is in the next indented part of the code
    if password_correct:                                        ## If the password is correct, then do this.
        print("Login successful! Welcome to your dashboard.")
    else:
        print("Incorrect Password. Please try again.")
else:
    print("Username not found. Please sign up.")
##############################################################################################################################

## Use nested if statements to check if a number is positive, negative, or zero.

number = int(input("Enter a number:\n"))

if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")

## Another way

if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")



## Normal Code
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("Access Granted")
else:
    print("Access Denied")
## Pseudocode
'''
PROMPT user for age
STORE input as user_age
IF user_age is greater than or equal to 18 THEN
DISPLAY "Access Granted"
ELSE
DISPLAY "Access Denied"
ENDIF
'''