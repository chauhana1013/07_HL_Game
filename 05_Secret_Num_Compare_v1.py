secret_num = 7
end_game = "no"
guess = int(input("Guess: "))

if guess < secret_num:
    print("Too low")

elif guess > secret_num:
    print("Too High")

else:
    guess = secret_num
    print("Yay, you guessed the Secret Number!!")

