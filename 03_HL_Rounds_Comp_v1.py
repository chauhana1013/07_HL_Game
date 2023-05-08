# Rounds Component Version 1 - The code works perfectly, but it can't fully be integrated into the base component

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


rounds_played = 0
# Ask user for # of rounds, press <ENTER> for Infinite Mode
rounds = rounds_checker()

game_over = "no"
while game_over == "no":

    print()
    # Rounds Heading
    if rounds == "":
        heading = f"Infinite Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        if rounds_played == rounds - 1:
            game_over = "yes"

    print(heading)
    guess = input("Guess: ")
    if guess == "xxx":
        break

    # Rest of game
    print(f"You chose {guess}")

    rounds_played += 1
# Thanks the player for playing after rounds finish
print("Thanks for playing")
