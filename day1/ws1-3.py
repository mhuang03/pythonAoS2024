# Problem 3: Fibonacci
# Write a program that asks the user for a number n and then prints the first n Fibonacci numbers.
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
# The sequence starts with 0 and 1.
# For example, the first 5 Fibonacci numbers are 0, 1, 1, 2, 3.
# Hint: Use some variables to keep track of the previous 2 Fibonacci numbers.

num = int(input("Enter a number: "))

prev_prev = 0
prev = 1
print(0)
print(1)

count = 2

while num != count:
    next_fib = prev_prev + prev
    print(next_fib)
    count += 1

    prev_prev = prev
    prev = next_fib

