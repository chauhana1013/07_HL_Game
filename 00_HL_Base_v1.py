import random


# Functions go here...


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


# Checks the user's input and ensures that the response is an integer
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    # If the user has entered a low number and a high number
    elif low is not None and high is not None:
        error = f"Please enter a number between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter a number that is more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too high etc.)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            # checks input is not too low
            elif situation == "low only":
                if response > low:
                    return response

            print(error)

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine go here...

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

rounds_played = 0
rounds_won = 0

mode = "regular"

print()
lowest = int_check("Low Number: ", 0)

highest = int_check("High Number: ", lowest)

rounds = int_check("Rounds: ", 0, exit_code="")
# Rounds loop
end_game = "no"
while end_game == "no":

    secret_num = random.randint(lowest, highest)

    if rounds == "":
        mode = "infinite"
        rounds = 5

    if mode == "infinite":
        heading = f"|♾♾♾ Infinite Mode ♾♾♾|Round {rounds_played + 1}"
        rounds += 1

    elif mode == "regular":
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Start Game
    while True:

        guess = int_check("Guess (type 'xxx' to quit): ", lowest, highest, "xxx")

        if guess == "xxx":
            end_game = "yes"
            break

        print("Pretend we've compared the number")

        if guess == secret_num:
            rounds_won += 1
            break

    if rounds_played >= rounds:
        break


print("Thanks for playing")
