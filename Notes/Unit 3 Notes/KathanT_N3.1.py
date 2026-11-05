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


## Two or Six
theoretical_probability = 1 / 3

two_or_six = 0

n = 101         ## Number of rolls

for i in range (n):
    roll=random.randint(1, 6)
    if roll == 2 or roll == 6:
        two_or_six += 1

experimental_probability = two_or_six / n


print("Theoretical Probability is: ", theoretical_probability)
print("Simulated Probability is: ", experimental_probability)


## Even Number
theoretical_probability = 1 / 2

even = 0

n = 101         ## Number of rolls

for i in range (n):
    roll=random.randint(1, 6)
    if roll % 2 == 0:
        even += 1

experimental_probability = even / n


print("Theoretical Probability is: ", theoretical_probability)
print("Simulated Probability is: ", experimental_probability)



## Sort and find the largest grade
grades = [40, 94, 97, 82, 89, 36, 87, 15, 87, 67, 69, 99]

grades.sort(reverse=True)
print(grades[0])

## The more difficult way Dr. Cummins showed
highest_grade = grades[0]

for grade in grades:
    if grade > highest_grade:
        highest_grade = grade

print(highest_grade)


## Find the Average of the grades
grades = [40, 94, 97, 82, 89, 36, 87, 15, 87, 67, 69, 99]
sum_of_grades = 0

for i in grades:
    sum_of_grades += i

average = sum_of_grades / len(grades)
print(average)


## Nested For Loops

## Times tables for 1 though 5
for i in range(1,6):
    for j in range(1,6):
        print(i * j, end = "\t")
    print()

## Count the number of passing grades
grades = [40, 94, 97, 82, 89, 36, 87, 15, 87, 67, 69, 99]

passing_grades = 0

for grade in grades:
    if grade >= 70:
        passing_grades += 1

print(passing_grades)