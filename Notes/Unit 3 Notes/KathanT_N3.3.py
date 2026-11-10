## For Loops
for x in range (1,11):
    print(x)

## While Loops
i = 1
while i <= 10:
    print(i)
    i += 1

## Suppose you start with $100, and your money doubles every year.
## How many years does it take to get $100,000?

money = 100
years = 0

while money < 100000:
    money *= 2
    years += 1

print(f"It took {years} years to make ${money}.")

## Predict the output
x = 2

while x < 15:
    print(x)
    x += 3

## Start with $0.
## Each day you make $13.
## Continue this process until you make $756.23.

savings = 0
day = 0
cost = 756.23
money_each_day = 420

while savings < cost:
    savings += money_each_day
    day += 1

print(f"You will have ${savings} in {day} days.\n${savings} is more than the ${cost} that you need.\nYou will have ${round((savings-cost), 2)} left over after your purchase.")
