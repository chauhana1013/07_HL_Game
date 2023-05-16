import math

for item in range(0, 4):
    low = int(input("Low Number: "))
    high = int(input("High Number: "))

    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print(f"Max Guesses: {max_guesses}")

    print()
