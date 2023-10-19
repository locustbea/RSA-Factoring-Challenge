#!/usr/bin//python3

import math


def prime_factorize(n):
    """Returns a list of the prime factors of n."""
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


# Example usage:
print(prime_factorize(100))
