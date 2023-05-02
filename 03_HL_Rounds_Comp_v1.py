# Rounds Component

# Round checker checks
def rounds_checker():
    while True:
        response = input("Rounds: ")

        rounds_error = "Please press <ENTER> or type in an integer more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(rounds_error)
                    continue
            except ValueError:
                print(rounds_error)
                continue

        return response


low_num = 1
high_num = 10
rounds_played = 0
guess_instructions = f"Guess a number between {low_num} and {high_num}"

rounds = rounds_checker()

game_over = "no"
while game_over == "no":

    print()
    if rounds == "":
        print()
        heading = f"Infinite Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        if rounds_played == rounds - 1:
            game_over = "yes"

    print(heading)
    guess = input("Guess: ")

    if guess == "xxx":
        break

    print(f"You chose {guess}")

    rounds_played += 1

print("Thanks for playing")
