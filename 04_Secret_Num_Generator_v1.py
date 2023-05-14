import random


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    # If the user has entered a low number and a high number
    elif low is not None and high is not None:
        error = f"Please enter a number between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter a number that is more than or equal to {low}"
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
                if response >= low:
                    return response

            print(error)

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine goes here...
end_game = "no"
while True:

    lowest = int_check("Low Number: ", 1)
    highest = int_check("High Number: ")

    if lowest >= highest:
        print(f"Highest Number should be more than {lowest}")
        continue
    secret_num = random.randint(lowest, highest)

    print(f"Secret number is {secret_num}")
