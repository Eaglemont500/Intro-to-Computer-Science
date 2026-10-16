import random

light = random.choice(["Red", "Yellow", "Green"])

if light == "Red":
    print("Stop")

elif light == "Yellow":
    print("Slow Down")

else:
    print("Go")