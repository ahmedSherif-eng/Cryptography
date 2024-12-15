"""Operations

This file contains all the operations of encryption & decryption.
Along with what we want to ensure.
"""


def encrypt(msg_plaintext, package):
    """encrypt

    This function encrypts the passed plaintext with the package, depending on whether
    we're trying to ensure authentication (package will hold private & n)
    or confidentiality (package will hold public & n).

    Arguments:
        msg_plaintext (str): The plaintext to encrypt.
        package (tuple): The keypair which could be either the public keypair or private keypair,
                         depending on whether we're trying to achieve authentication or confidentiality.

    Return:
        (int): The ciphertext after encryption.
    """
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext


def decrypt(msg_ciphertext, package):
    """decrypt
        
    This function decrypts the passed ciphertext with the package, depending on whether
    we're trying to ensure authentication (package will hold public & n) or
    confidentiality (package will hold private & n).

    Arguments:
        msg_ciphertext (int): The ciphertext to decrypt.
        package (tuple): The keypair which could be either the public keypair or private keypair,
                         depending on whether we're trying to achieve authentication or confidentiality.

    Return:
        (str): The plaintext after decryption
    """
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    return ''.join(msg_plaintext)


def confidentiality(msg, public, private, flag):
    """confidentiality

    This function encrypts the message while ensuring confidentiality

    Arguments:
        msg (str): The message to be encrypted/decrypted.
        public (int): The public key.
        private (int): The private key.
        flag (int): If 0 will encrypt otherwise will decrypt

    Return:
        (str || int): Ciphertext if encryption, Plaintext if decryption
    """
    if flag == 0:
        encrypted_msg = encrypt(msg, public)
        print("Encrypted msg: ", end="")
        print(''.join(map(lambda x: str(x), encrypted_msg)))
        return encrypted_msg
    else:
        decrypted_msg = decrypt(msg, private)
        print(f"Decrypted msg: {decrypted_msg}")
        return decrypted_msg


def authentication(msg, public, private, flag):
    """authentication

    This function encrypts the message while ensuring confidentiality

    Arguments:
        msg (str): The message to be encrypted/decrypted.
        public (int): The public key.
        private (int): The private key.
        flag (int): If 0 will encrypt otherwise will decrypt

    Return:
        (str || int): Ciphertext if encryption, Plaintext if decryption
    """
    if flag == 0:
        encrypted_msg = encrypt(msg, private)
        print("Encrypted msg: ", end="")
        print(''.join(map(lambda x: str(x), encrypted_msg)))
        return encrypted_msg
    else:
        decrypted_msg = decrypt(msg, public)
        print(f"Decrypted msg: {decrypted_msg}")
        return decrypted_msg
