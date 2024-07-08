low = 0
high = 101
guess_count = 0

while True:
    guess = low + (high - low)//2
    print(f"I guess {guess}")
    guess_count += 1

    result = input("Was my guess too high (H), too low (L), or correct (C)? ")

    if result == "H":
        high = guess
    elif result == "L":
        low = guess
    elif result == "C":
        print(f"I won in {guess_count} guesses!")
        break
