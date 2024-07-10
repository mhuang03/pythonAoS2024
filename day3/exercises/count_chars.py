string = "aaaaabbbbbcccabcacbcbacbacba4f3th0239"

counts = {}

for char in string:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)