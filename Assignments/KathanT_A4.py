length = float(input("What is the length of your rectangle? (Positive values only.) "))
if length <= 0:
    print(length , " is not a valid length.")
    exit()

width = float(input("What is the width of your rectangle? (Positive values only.) "))
if width <= 0:
    print(width , " is not a valid width.")
    exit()

area = length * width
perimeter = (2 * length) + (2 * width)

print("The area of your rectangle is " , area , " units.")
print("The perimeter of your rectangle is " , perimeter , " units.")


y=10
z=20/2
y==z