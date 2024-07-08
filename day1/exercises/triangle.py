x = int(input("Enter a side length: "))
y = int(input("Enter a side length: "))
z = int(input("Enter a side length: "))

if x + y > z and y + z > x and x + z > y:
    print("Valid Triangle!")
else:
    print("Not a valid triangle :(")