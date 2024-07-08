num = int(input("Enter a number: "))
steps = 0

while num != 1:
    print(num)
    # apply logic
    if num % 2 == 0:
        num = num//2
    else:
        num = num*3+1
    steps += 1

print(1)
print(f"That took {steps} steps!")