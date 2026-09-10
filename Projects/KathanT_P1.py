## First Portion (Madlibs)


## Asking for inputs from user
name = input("Enter a name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
food = input("Enter a food: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
number = input("Enter a number: ")

## Using inputs in story
story = f"{name} was casually strolling through the {place} when a {adjective} {animal} dropped directly from the ceiling. The creature let out a terrifying shriek and immediately began to {verb} right in the middle of the floor! Desperate to survive, {name} grabbed {number} {food}s and hurled them as a distraction. To everyone's shock, the {animal} caught the {food}s in mid-air, burped loudly, and bowed politely. {name} slowly backed away and sprinted for the exit, vowing to never run errands on a Tuesday again."

## Prints story
print(story)



## Second Portion


## Asks user for 2 coordinate pairs
while True:
    try:
        xsub1 = float(input("Enter x\u2081: "))
        ysub1 = float(input("Enter y\u2081: "))
        xsub2 = float(input("Enter x\u2082: "))
        ysub2 = float(input("Enter y\u2082: "))
        break
    except ValueError:
        print("Please enter valid numbers")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram Terminated")
        exit()

## Does calculations for distance and midpoint
distance = round((((xsub2 - xsub1) ** 2) + ((ysub2 - ysub1) ** 2)) ** 0.5, 3)
midpoint = ((xsub1 + xsub2) / 2) , ((ysub1 + ysub2) / 2)

## Does calculations for slope, with error handeling for division by zero
if xsub2 - xsub1 != 0:
    slope = round((ysub2 - ysub1) / (xsub2 - xsub1), 3)
else:
    slope = "Undefined"

## Takes previous info and plugs it into pointslope form
if xsub1 == xsub2 and ysub1 == ysub2:
    pointslope = "Infinitely many lines (Identical points)"
elif xsub1 == xsub2:
    pointslope = f"x = {xsub1}"
elif ysub1 == ysub2:
    pointslope = f"y = {ysub1}"
else:
    ysign = "+" if ysub1 < 0 else "-"
    xsign = "+" if xsub1 < 0 else "-"
    pointslope = f"y {ysign} {abs(ysub1)} = {slope}(x {xsign} {abs(xsub1)})"

## Prints the different numbers
print(f"The distance is: {distance}")
print(f"The midpoint is: {midpoint}")
print(f"The slope is: {slope}")
print(f"The formula is: {pointslope}")