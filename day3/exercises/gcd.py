def gcd(a, b):
    start = min(a, b)

    for i in range(start, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(gcd(50, 75))