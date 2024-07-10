def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def print_primes(k):
    count = 0
    num = 2
    while count < k:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

print_primes(5)