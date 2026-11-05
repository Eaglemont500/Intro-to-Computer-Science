## For Loops
'''
for i in range(5):
    print(i)

## Range starts at 0 and ends at the integer before the integer in the argument

for i in range(1,6):
    print(i)

## Only want even numbers from 0 to 1000

for i in range(0, 1001, 2):
    print(i)

## Sum of the first 100 positive integers

total = 0

for i in range(1, 101):
    total += i
print(total)

## 7 Times Tables
number = 7

for chud in range(1,13):        ## Does not have to be "i"
    print(number, "x", chud, "=", number * chud)

## Every square between 1 and 10

for i in range(1,11):
    if i**2 % 3 == 0:
        print(i**2)

        
## Dice Example
import random

theoretical_probability = 1 / 6

sixes = 0

n = 100

for i in range (n):
    roll=random.randint(1, 6)
    if roll == 6:
        sixes += 1

experimental_probability = sixes / n


print("Theoretical Probability is: ", theoretical_probability)
print("Simulated Probability is: ", experimental_probability)

'''

## Sort and find the largest grade
grades = [94, 97, 82, 89, 36, 87, 15, 87, 67, 69, 99]

grades.sort(reverse=True)
print(grades[0])

## The more difficult way Dr. Cummins showed
highest_grade = grades[0]

for grade in grades:
    if grade > highest_grade:
        highest_grade = grade

print(highest_grade)