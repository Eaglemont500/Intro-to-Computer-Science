'''
print("\033[H\033[J", end="") 
n = int(input("Enter a Number:\n"))
count = 0
while n != 1:
    if n % 2 == 0:
        n/=2
        print(int(n))
    else:
        n*=3
        n+=1
        print(int(n))
    count += 1
print(f"It took {count} iterations to get to 1.")
'''
money = 1000
years = 0

while money < 5000:
    money *= 1.05
    years += 1

print(f"It would take {years} years to make $5000. You would have ${money} after {years} years.")

n = 101
while n % 7 != 0 or n % 11 != 0:
    n += 1
print(n)