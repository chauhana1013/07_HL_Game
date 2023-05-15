secret_num = 7

while True:
    guess = int("Guess: ")

    if guess < secret_num:
        print("Too low")

    elif guess > secret_num:
        print("Too High")
    elif guess == secret_num: 