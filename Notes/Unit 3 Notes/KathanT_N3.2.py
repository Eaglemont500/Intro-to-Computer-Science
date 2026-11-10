'''for i in range (10):
    if i == 5:
        break   ## Break stops at 5
    print(i)

for i in range (10):
    if i == 5:
        continue   ## Continue skips 5
    print(i)
'''
## Sum of perfect squares between 1 and 100 that are divisible by three
sum = 0
for i in range (11):
    if i ** 2 % 3 == 0:
        sum += i ** 2
print(sum)

## Print first hundred integers, but not 13
for i in range (101):
    if i == 13:
        continue
    print(i)