'''
base10 = int(input("Enter a Base 10 number to convert to Binary\n"))

binary = bin(base10)
binary = binary.removeprefix("0b")

print(binary)
'''

while True:
    try:
        base10 = int(input("Enter a Base 10 integer to convert to Binary (between 0 and 31)\n"))
    except ValueError:
        print("Please enter an integer.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram terminated")
        exit()

    if base10 > 31:
        print("Please enter a smaller number.")
<<<<<<< HEAD
    elif base10 < 0:
=======
    if base10 < 0:
>>>>>>> 15125fb80d79e78df7d7630c37fbbf53d39a2fa5
        print("Please enter a larger number.")
    else:
        break
place0 = base10 % 2
base10 = base10 // 2
place1 = base10 % 2
base10 = base10 // 2
place2 = base10 % 2
base10 = base10 // 2
place3 = base10 % 2
base10 = base10 // 2
place4 = base10 % 2

binary = f"{place4}{place3}{place2}{place1}{place0}"

print(f"Your Base10 number in binary is {binary}.")