import os
from math import gcd
from random import randint


def is_prime(n):
    """
    This function receives a number - n.
    It returns whether n is prime or not.
    Time complexity is O(n**0.5) in the worst case.
    """

    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    # Looping until i reaches the square root of n
    for i in range(4, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


