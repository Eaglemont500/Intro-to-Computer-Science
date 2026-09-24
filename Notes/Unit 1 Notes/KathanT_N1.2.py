## Errors
SyntaxError ## Disobeying the rules of the language
'''
print(5))
print("5)
'''


## Logical Errors 
## Program will run, but with incorrect logic 

## Manually find the average of a set of numbers
'''
average = (1+2+3+5+4+6+7)/6
'''
## Will run, but not correct math


RuntimeError ## Impossible logic
## ZeroDivisionError
'''
a = 3
b = 3
c = 4
d = 1

x = b - a
y = c - d

slope = y / x
'''

## IndexError
'''
a = [1 , 2 , 3 , 4]
a [0]
a [1]
a [4]
'''


OverflowError ## Storing too much information into a variable
## Integers that are greater than 2147483647 cannot be stored




## Incrementing variables
x = 2
x = x + 1 ## x = 3
x = x**2 ## x = 9
x = x // 2 ## x = 4
x = x - 2 ## x = 2

print(x)

# Sets
numbers = {1 , 2 , 3 , 5 , 5 , 5 , 7}
values = {10}

amount1 = numbers - values
amount2 = numbers + values

print(amount1)
print(amount2)