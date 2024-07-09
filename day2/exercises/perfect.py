count = 0
num = 1

while count < 4: # find the first 4 perfects
    factor_sum = 0

    # add all factors up
    for i in range(1, num):
        if num % i == 0:
            factor_sum += i

    if factor_sum == num:
        print(num) # found perfect number!
        count += 1

    num += 1
