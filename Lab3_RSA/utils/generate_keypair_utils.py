"""generate_keypair_utils.py

This file contains the utilites for the generate_keypair function of
the RSA algorithm.
"""

from typing import List
import random
from .utils import gcd, modInverse


def getRange(keysize # type: int
            ):
    """getRange

    This function gets the helper range values to be used
    across the RSA algorithm.
    
    Arguments:
        keysize (int): The keysize for the algorithm.

    Return:
        (int, int, int, int): The returned values are:
                              1. nMin: The minimum 
                              2. nMax: The maximum
                              3. start: The starting prime.
                              4. stop: The ending prime.
    """
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)
    return nMin, nMax, start, stop


def createPrimeList(primes, start, stop):
    """createPrimeList

    Arguments:
        primes (List): The initial list of primes.
        start (int): The starting point.
        stop (int): The ending point.

    Return:
        (List): The primes between start & stop.
    """
    if start >= stop:
        return []
    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    return primes


def removeNotInRange(primes, #type: List[int]
                     start #type: int
                    ):
    """removeNotInRange

    This function removes all the prime numbers that are generated that
    aren't in the specified starting range.

    Arguments:
        primes (list): The generated primes.
        start (int): The starting point.
    """
    print(f"Primes before the while loop {primes}")
    while primes and primes[0] < start:
        del primes[0]
    print(f"Primes after the while loop {primes}")


def choosePrimes(primes, # type: List[int]
                 p, # type: int
                 q, # type: int
                 nMin, #type: int
                 nMax #type: int
                ):
    """choosePrime

    This function takes the generated prime list and chooses the
    best 2 prime numbers that fit range of:
    - nMin <= p * q <= nMax 

    Arguments:
        primes (List): The prime number list generated
        p (int): Initial random int (0 - 1000)
        q (int): Initial random int (0 - 1000)
        nMin (int): The minimum threshold
        nMax (int): The maximum threshold

    Return:
        (int, int): The 2 chosen prime numbers p & q
    """
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
    return p, q


def generatePublicandPrivate(p, # type: int
                             q # type: int
                            ):
    """generatePublicandPrivate

    This function generates the public & private key to be used
    in encryption & decryption.

    Arguments:
        p (int): The 1st chosen prime number
        q (int): The 2nd chosen prime number

    Return:
        (int, int): The public & private key pair.
                    1. e: Public key
                    2. d: Private key
    """
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi) # 1 < e < phi(n)
    g = gcd(e, phi)
    while True:
        # as long as gcd(1,phi(n)) is not 1, keep generating e
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        # generate private key
        d = modInverse(e, phi)
        if g == 1 and e != d:
            break
    return e, d