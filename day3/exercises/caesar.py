alphabet = "abcdefghijklmnopqrstuvwxyz"
map = {}
shift = 5

for i in range(26):
    map[alphabet[i]] = alphabet[(i + shift) % 26]

message = "Hello World!".lower()
encoded = ""

for char in message:
    if char in map:
        encoded += map[char]
    else:
        encoded += char

print(encoded)