"""RSA

This file contains the RSA algorithm code
"""
from utils import createPrimeList, getRange, removeNotInRange, choosePrimes, generatePublicandPrivate
from utils import authentication, confidentiality
import random


# initial two random numbers p,q
p = random.randint(1, 1000)
q = random.randint(1, 1000)


def generate_keypair(p, q, keysize):
    """generate_keypair

    This function generates the keypair (public & private) for performing
    the RSA encryption & decryption.

    Arguments:
        p (int): Random number
        q (int): Random number
        keysize (int): The bit size.

    Return:
        ((int, int), (int, int)): 2 pairs. The first pair for the public & the second for the private.
                        Output format: public key (e,n) & private key (d,n)
    """
    primes = [2]
    nMin, nMax, start, stop = getRange(keysize)
    print(f"start = {start} stop = {stop}")

    createPrimeList(primes, start, stop) # Passed by reference
    removeNotInRange(primes, start) # Passed by reference

    # choosing p and q from the generated prime numbers.
    p, q = choosePrimes(primes, p, q, nMin, nMax)
    print(f"The choosen p = {p} & q = {q}")

    n = p * q
    e, d = generatePublicandPrivate(p, q)

    return (e, n), (d, n)


if __name__ == "__main__":
    bit_length = int(input("Enter bit_length: "))
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(p, q,  bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    msg = input("Write msg: ")
    # print([ord(c) for c in msg]) # Prints ascii for each letter
    choice = int(input("Choose which you want to ensure:\n1. Authentication\n2. Confidentiality\nChoice: "))
    if choice == 1:
        encrypt_msg = authentication(msg, public, private, 0)
        decrypt_msg = authentication(encrypt_msg, public, private, 1)
    else:
        encrypt_msg = confidentiality(msg, public, private, 0)
        decrypt_msg = confidentiality(encrypt_msg, public, private, 1)