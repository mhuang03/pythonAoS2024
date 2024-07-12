# Problem 3: Anagrams
# Design a function that accepts two strings and returns True if the strings are anagrams,
# and False otherwise. Anagrams are words or phrases that are formed by rearranging the
# letters of another word or phrase, using all the original letters exactly once.
# For example, "listen" and "silent" are anagrams.
# Hint: You could: 1) use a dictionary to store the counts of each letter in each string.
#               or 2) sort the letters in each string and compare the sorted strings.

def is_anagram(s1, s2):
    letters = {}
    for char in s1:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    for char in s2:
        if char not in letters:
            return False
        else:
            letters[char] -= 1

    for val in letters.values():
        if val != 0:
            return False
    return True


def is_anagram_2(s1, s2):
    return sorted(s1) == sorted(s2)


print(is_anagram("silent", "listen"))
print(is_anagram_2("silent", "listen"))
print(is_anagram("silenta", "listen"))
print(is_anagram_2("silenta", "listen"))