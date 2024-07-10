# Problem 2: Triangle
# Write a program that asks the user for a number n and then prints a triangle with n rows.
# For example, if the user enters 5, the program should print:
# *
# **
# ***
# ****
# *****
# Hint: Use nested loops to print the rows of the triangle. Use print(text, end='') to print on the same line.

num = int(input("Enter the number of rows: "))

for i in range(num):
    for j in range(i+1):
        print("*", end="  ")
    print()