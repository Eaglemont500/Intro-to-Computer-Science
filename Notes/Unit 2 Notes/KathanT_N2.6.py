age = int(input("Enter your age (Integers only)\n"))
season_pass = input("Do you have a season pass? (y/n)\n").strip().lower()

if age <= 12:
    if season_pass == "y":
        price = 5
    else:
        price = 15
elif age <= 65:
    if season_pass == "y":
        price = 10
    else:
        price = 30
else:
    if season_pass == "y":
        price = 3
    else:
        price = 8 

print(f"Your price is ${price}!")