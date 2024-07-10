prices = {"apple": 2.50, "orange": 3, "banana": 1}

print("Welcome to my shop!")
item = input("What would you like to buy? ")
total = 0
while item != "done":
    if item in prices:
        total += prices[item]
    else:
        print("We don't sell that...")

    item = input("What would you like to buy? ")

print(f"Your total is: ${total:.2f}")