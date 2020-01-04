"""
Name: Matt Robinson
Filename: affine.py
Description: Implement the affine cipher decryption and encryption algorithms
Language: Python
"""
import math


def encrypt(plaintext, k1, k2, mod):
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
    decrypted_text = ""
    if gcd(k1, mod) == 1 and 1 <= k2 <= mod and 1 <= k1 <= mod:
        for c in ciphertext.lower():
            a_prime = mult_inverse(k1, mod)
            decrypted_text += chr((a_prime*((ord(c)-97) - k2)) % mod + 97)
    else:
        print("Operation could not be completed")
    return decrypted_text


def mult_inverse(a, m):
    for i in range(1,m):
        if a*i % m == 1:
            return i


def gcd(a,m):
    return math.gcd(a,m)


if __name__ == "__main__":
    ciphertext = encrypt("Hello my name is matt",3,7,26)
    print(ciphertext)
    plaintext = decrypt(ciphertext,3,7,26)
    print(plaintext)