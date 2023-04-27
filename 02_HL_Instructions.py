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


print("⬆⬆⬆ Welcome to the Higher Lower Game ⬇⬇⬇")
show_instructions = yes_no("Would you like to see the Instructions? ")
if show_instructions == "yes":
    print("⬆⬆⬆ Instructions ⬇⬇⬇")
    print()
    print("First ")