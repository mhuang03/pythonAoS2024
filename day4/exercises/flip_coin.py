from random import choice

coin = ["Heads", "Tails"]
flip_result = choice(coin)

answer = input("Heads or Tails? ")
if answer == flip_result:
    print("You got it!")
else:
    print("nah")