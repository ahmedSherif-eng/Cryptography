"""utils

This file contains the helper functions needed to run the RSA algorithm
"""

from math import sqrt


def gcd(a, b):
    """gcd

    This function calcualtes the Greates Common Divisor of
    2 numbers.
    
    Arguments:
        a (int): The first number.
        b (int): The second number.

    Return:
        (int): The greatest common divisor.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def modInverse(a, m):
    """mod_inverse

    This function calcualtes the inverse of a mod.

    Arguments:
        a (int): The number before the modulo.
        m (int): The number after the modulo.

    Return:
        (int): The mod inverse.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def isPrime(n):
    """isprime

    This function checks whether a passed number is prime or not.

    Arguments:
        n (int): The number.
    
    Return:
        (bool): True if n is prime, false otherwise.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True
