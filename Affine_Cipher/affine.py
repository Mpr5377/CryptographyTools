"""
Name: Matt Robinson
Filename: affine.py
Description: Implement the affine cipher decryption and encryption algorithms
Language: Python
"""
import math


def encrypt(plaintext, k1, k2, mod):
    """
    Function: encrypt
    Description: Use the affine cipher to encrypt the plaintext
    :param plaintext: The text to be encrypted
    :param k1: The first part of the key
    :param k2: The second part of the key
    :param mod: The length of the alphabet
    :return: The encrypted message
    """
    encrypted_text = ""
    plaintext = plaintext.split(" ")
    plaintext = "".join(plaintext)
    if gcd(k1,mod) == 1 and 1 <= k2 <= mod and 1 <= k1 <= mod:
        for c in plaintext.lower():
            encrypted_text += chr(((k1 * (ord(c)-97)) + k2) % mod+97)
    else:
        print("Operation could not be completed")
    return encrypted_text


def decrypt(ciphertext, k1, k2, mod):
    """
    Function: Decrypt
    Description: Decrypt the ciphertext to plaintext
    :param ciphertext: The text to be decrypted
    :param k1: The first part of the key
    :param k2: The second part of the key
    :param mod: The length of the alphabet
    :return: The decrypted message
    """
    decrypted_text = ""
    if gcd(k1, mod) == 1 and 1 <= k2 <= mod and 1 <= k1 <= mod:
        for c in ciphertext.lower():
            a_prime = mult_inverse(k1, mod)
            decrypted_text += chr((a_prime*((ord(c)-97) - k2)) % mod + 97)
    else:
        print("Operation could not be completed")
    return decrypted_text


def mult_inverse(a, m):
    """
    Function: mult_inverse
    Description: Given a number a, and the modulo m, find the multiplicative inverse of a
    :param a: The number to find the multiplicative inverse of
    :param m: The modulo
    :return: The multiplicative inverse of a
    """
    for i in range(1,m):
        if a*i % m == 1:
            return i


def gcd(a,m):
    """
    Function: gcd
    Description: Finds the greatest common divisor of a and m
    :param a: The smaller number
    :param m: The larger number
    :return: The greatest common divisor of a and m
    """
    return math.gcd(a,m)


if __name__ == "__main__":
    ciphertext = encrypt("Hello my name is matt",3,7,26)
    print(ciphertext)
    plaintext = decrypt(ciphertext,3,7,26)
    print(plaintext)