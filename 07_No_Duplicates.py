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


secret_num = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed

guess = ""

while guess != secret_num and guesses_left >= 1:

    guess = int_check("Guess: ")

    # If user's current guess has already been guessed before, displays error message
    # and user has the same number of guesses
    if guess in already_guessed:
        print(f"You've already guessed {guess}! You still have {guesses_left} guesses left.")
        continue

    # If user's guess has not been guessed before, it is added to the already_guessed list
    guesses_left -= 1
    already_guessed.append(guess)
