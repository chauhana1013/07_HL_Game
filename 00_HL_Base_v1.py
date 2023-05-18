import random
import math

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
# Shows different error messages depending on what type of parameter is involved
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"

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
rounds_lost = 0

all_scores = []

mode = "regular"

print()
lowest = int_check("Low Number: ", 0)
highest = int_check("High Number: ", lowest)

# Generates the total number of guesses the user gets per round
# depending on the range between the highest number and the lowest number
print()
var_range = highest - lowest + 1
max_raw = math.log2(var_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1

rounds = int_check("Rounds: ", 0, exit_code="")

# If user presses <ENTER>, Infinite Mode is selected
if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop
end_game = "no"
while end_game == "no":

    already_guessed = []

    guesses_allowed = max_guesses

    secret_num = random.randint(lowest, highest)
    print(f"Spoiler alert : {secret_num}")

    if mode == "infinite":
        heading = f"|♾♾♾ Infinite Mode ♾♾♾|Round {rounds_played + 1}"
        rounds += 1

    elif mode == "regular":
        heading = f"Round {rounds_played + 1} of {rounds}"

    print()
    print(heading)

    rounds_played += 1

    # Start Game
    while True:

        # Asks the user to guess
        guess = int_check("Guess (type 'xxx' to quit): ", lowest, highest, "xxx")

        # If user's current guess has already been guessed before, displays error message
        # and user has the same number of guesses
        if guess in already_guessed:
            print(f"You've already guessed {guess}! You still have {guesses_allowed} guesses left.")
            continue

        # If user's guess has not been guessed before, it is added to the already_guessed list
        guesses_allowed -= 1
        already_guessed.append(guess)

        # Game over if user inputs exit code
        if guess == "xxx":
            end_game = "yes"
            break

        # If guess is less than the secret number, outputs the guess was too low
        # and shows total number of guesses left
        elif guess < secret_num:
            print(f"⬇⬇⬇ Too Low ⬇⬇⬇ | Guesses Left: {max_guesses}")

        # If guess is more than the secret number, outputs the guess was too high
        # and shows total number of guesses left
        elif guess > secret_num:
            print(f"⬆⬆⬆ Too High ⬆⬆⬆ | Guesses Left: {max_guesses}")

        # If user guesses the secret number, they win the round
        if guess == secret_num:
            print("🥳🥳🥳~|Yay, you guessed the Secret Number|~🥳🥳🥳")
            rounds_won += 1
            break

        # If the user runs out of guesses, they lose the round and the Secret Number is revealed
        if guesses_allowed == 0:
            print()
            print("😢😢😢~|Unlucky, you lost the round|~😢😢😢")
            print()
            print(f"|The Secret Number was {secret_num}|")
            rounds_lost += 1
            break

        print()

    # Game Over if all rounds played
    if rounds_played >= rounds:
        break

print("Thanks for playing")
