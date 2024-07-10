nested = [[5, 6, 7], [2, 3], [10, 11, 12], [5]]

flat = []
for inner in nested:
    for item in inner:
        flat.append(item)

print(flat)