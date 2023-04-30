# Functions go here...

#
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes or no")
            print()


# Number checking function goes here
def int_check(question, low=None, high=None):

    situation = ""
    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or
            # too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue
            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than (or equal to) {low}")
                    continue

            return response

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue

# Main Routine go here...

# Introduces the user to the game and 
print("⬆⬆⬆ Welcome to the Higher Lower Game ⬇⬇⬇")
show_instructions = yes_no("Would you like to see the Instructions? ")
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

elif show_instructions == "no":
    print("Program Continues")


lowest = int_check("Low Number: ")
highest = int_check("High Number: ")
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess ", lowest, highest)