string = input("Type something: ")
chars = set()

for char in string:
    chars.add(char)

print(f"You typed {len(chars)} unique characters")