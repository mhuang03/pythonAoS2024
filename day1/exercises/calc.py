x = int(input("Give me a number: "))
op = input("Operation: ")
y = int(input("Give me another number: "))

if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    if y == 0:
        print("Can't divide by 0!!!!!!")
    else:
        print(x/y)
else:
    print("that's not a real operation")