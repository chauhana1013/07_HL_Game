# Instructions Component

# Checks user input for the question and
# if user inputs anything apart from 'yes' or 'no', displays error message
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        # Displays Error Message
        else:
            print("Please answer yes or no")
            print()


# Introduces the user to the game and asks the user if they would like to view the Instructions
print("⬆⬆⬆ Welcome to the Higher Lower Game ⬇⬇⬇")
show_instructions = yes_no("Would you like to see the Instructions? ")

# If user answers 'yes', it Displays the Instructions
if show_instructions == "yes":
    print("⬆⬆⬆ Instructions ⬇⬇⬇")
    print()
    print("Choose your Minimum and Maximum numbers as the range for the secret number")
    print("Then choose how many rounds you want to play")
    print()
    print("The computer will automatically generate how guesses you get for each round, "
          "depending on the Lowest and Highest number")
    print()
    print("The aim of the game is to guess the secret number and if you guess higher or lower than the secret number, "
          "the computer will tell you")
# If user answers 'no', Program Continues
elif show_instructions == "no":
    print("Program Continues")
