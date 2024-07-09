string = input("type something: ")

count = 0
for char in string:
    if char in "aeiouAEIOU":
        count += 1

print(f"You typed {count} vowels!")