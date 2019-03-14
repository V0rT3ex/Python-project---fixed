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


def generate_prime_file(a, path):
    """
    This function creates a list of prime numbers under the upper boundary denoted by a.
    It also writes the list to a file.
    """

    # Creating a list of prime numbers.
    prime_list = [i for i in range(a + 1) if is_prime(i)]

    # Opening a file in the path passed as a parameter, to write to.
    with open(path, mode='wt', encoding='utf-8') as f:
        # Writing each number to the file delimited by comma(,).
        for number in prime_list:
            f.write(str(number) + ",")


def generate_primes(path):
    """
    This function receives a path of a file.
    The file contains prime numbers which will be read into a list.
    The function returns two different random prime numbers - p and q.
    If an error occurs, p and q will be -1 in default.
    """

    p, q = -1, -1

    # Opening a file to read from the prime numbers.
    with open(path, mode='rt', encoding='utf-8') as f:
        chunk_size = 256
        # Reading from the file until there is no content.
        prime_list = f.read(chunk_size)
        while True:
            content = f.read(chunk_size)
            if not content:
                break
            prime_list += content
        # Transforming the data from str to a list and delimiting by the comma.
        prime_list = prime_list.split(',')
        # Setting the list to be from its beginning to the end excluding the last item.
        prime_list = prime_list[:-1]

        # Looping until p and q, two random numbers from the list, are different.
        while True:
            p = int(prime_list[randint(0, len(prime_list) - 1)])
            p = int(prime_list[randint(0, len(prime_list) - 1)])
            if p != q:
                break
    return p, q
