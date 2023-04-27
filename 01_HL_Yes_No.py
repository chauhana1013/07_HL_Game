show_instructions = ""
while show_instructions != "xxx":
    # Ask user if they would like to see the Instructions
    show_instructions = input("Would you like to see the Instructions? ").lower()

    # If user says 'yes', output 'Display Instruction'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Display Instructions")

    # If user says 'no', output 'Program Continues'
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Program Continues")

    # If user says something else, displays error message
    else:
        print("Please answer yes or no")