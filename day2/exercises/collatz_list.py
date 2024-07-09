num = int(input("Enter a number: "))

sequence = [num]
largest = num

while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num*3 + 1
    sequence.append(num)

    if num > largest:
        largest = num

print(sequence)
print(len(sequence))
print(f"The largest value was {largest}!")