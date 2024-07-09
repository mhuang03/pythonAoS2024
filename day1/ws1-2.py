# Problem 2: Factorial
# Write a program that asks the user for a number n and then calculates the factorial of that number.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# Hint: Use a loop to multiply the numbers from 1 to n together.

num = int(input("Enter a number: "))
result = num

while num > 1:
    num -= 1
    result *= num

print(result)

