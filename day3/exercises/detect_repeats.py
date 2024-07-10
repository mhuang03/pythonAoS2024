words = set()
for _ in range(5):
    word = input("Type a word: ")
    words.add(word)

if len(words) < 5:
    print("You repeated a word")
else:
    print("No repeats!")