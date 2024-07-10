# Problem 1: No Numbers or Vowels
# Write a program that asks the user for a string and then prints the string without any numbers or vowels.
# For example, if the user enters "Hello 123 World", the program should print "Hll Wrld".
# Hint: Use a loop to iterate over the characters in the string and check if each character is a number or a vowel.

string = input("Enter some text: ")

result = ""

for char in string:
    if char not in "aeiouAEIOU1234567890":
        result += char

print(result)
