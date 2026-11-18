## Convert Farenheit to Celsius
tempF1 = 77

tempC1 = (tempF1 - 32) * (5 / 9)

print(tempC1)


tempF2 = 98.6

tempC2 = (tempF2 - 32) * (5 / 9)

print(tempC2)

## Function
## We need "def" to start a function
## The function will have a name
## Has an arguement (like an input), sometimes multiple arguements

## If you want to save and print an output of the function, you need to use return
## Return stops your function; There should only be one return inside of a function

## Uses return
def F_to_C(farenheit):
    return (farenheit - 32) * (5 / 9)

print(F_to_C(77))
print(F_to_C(100))
print(F_to_C(0))

## Does not use return
name = input("Please tell me your name:\n")
def message(name):
    print(f"Hello {name}!")

message(name)

## Make a function that inputs the coefficients of a quadratic function, and then solve the quadratic equation
def quadratic_quation(a, b, c):
    return [(-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a), (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)]
    
print(quadratic_quation(1, 5, 6))


## Calculate area of a triangle
def triangle_area(b, h):
    return 0.5 * b * h

print(triangle_area(6, 5))

## Checks if a number is even or odd
def even_or_odd(x):
    if(x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))


def quadratic(a, b, c):
    x1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    x2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    return x1, x2

x1, x2 = quadratic(1, 5, 6)

print(x1)
print(x2)

## Check if a number is prime
def is_prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
for n in range(3,101):
    if is_prime(n):
        print(n)

def is_prime2(n):
    for i in range (2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True
for n in range(3,1000001):
    if is_prime2(n):
        print(n)
