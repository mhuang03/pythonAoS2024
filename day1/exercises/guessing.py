import random
ans = random.randint(1, 100)

guess = int(input("Guess the number: "))
while guess != ans:
    if guess < ans:
        print("too low")
    elif guess > ans:
        print("too high")
    guess = int(input("Guess the number: "))

print("you win!")