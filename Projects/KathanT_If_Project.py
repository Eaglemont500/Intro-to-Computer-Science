try:
    ## Prints title and Description
    print("\033[H\033[J", end="") 
    print("Welcome to The Outfit Recommender!\nThis is a project that will recommend what you should wear based on the temperature, the current weather, and the occasion.")

    ## Asks for Inputs
    ## Converts user inputs to lowercase
    ## Makes sure user enters a predefined option
    ## The lines that say "print("\033[H\033[J", end="")" are to clear the terminal.
    while True:
        temp = input("What is the current temperature? (\u00B0F please)\n")
        try:
            temp = float(temp) 
        except ValueError:
            print("\033[H\033[J", end="") 
            print("Invalid Input!\nPlease enter a number.")
            continue
        raining = input("Is it raining? (y/n)\n").strip().lower()
        if raining not in ["y", "n",]:
            print("\033[H\033[J", end="") 
            print("Invalid Input!\nPlease enter 'y' for Yes and 'n' for No.")
            continue
        occasion = input("What is the occasion? (School, Sports, or Formal Event)\n").strip().lower()
        if occasion not in ["school", "sports", "formal event"]:
            print("\033[H\033[J", end="") 
            print("Invalid Input!\nPlease choose one of the options")
            continue
        break

    ## Recommend clothing based on Weather
    if temp < 32:
        print("Wear a Heavy Winter Coat.")
    elif temp < 50:
        print("Wear a Jacket.")
    elif temp < 75:
        print("Wear a Light Layer or Regular Outfit.")
    else:
        print("Wear lightweight clothing.")

    ## Recommend whether to bring an umbrella or not
    if raining == "y":
        print("Bring an Umbrella.")
    else:
        print("No Umbrella is required.")

    ## Recommend clothing based on occasion
    if occasion == "school":
        print("Wear a comfortable, casual outfit.")
    elif occasion == "sports":
        print("Wear athletic clothing and sneakers.")
    else:
        print("Wear dressier clothing.")
except (EOFError, KeyboardInterrupt):
    print("\033[H\033[J", end="") 
    print("Program Terminated")
    exit()