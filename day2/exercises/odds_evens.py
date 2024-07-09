my_list = [2, 6, 7, 14, 5, 9]
odds = []
evens = []

for val in my_list:
    if val % 2 == 0:
        evens.append(val)
    else:
        odds.append(val)

print(evens)
print(odds)