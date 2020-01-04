"""
Filename: caesar.py
Name: Matt Robinson
Description: Demonstrating a caesar cipher's encrypt and decryption functions
Language: Python
"""
def encrypt(plaintext, shift):
    encrypted_string = ""
    for c in string:
        encrypted_string += chr(ord(c) + shift % 26)
    return encrypted_string


def decrypt(ciphertext, shift):
    decrypted_string = ""
    for c in ciphertext:
        decrypted_string += chr(ord(c) - shift % 26)
    return decrypted_string


if __name__ == '__main__':
    string = "Hello Matt"
    shift = 3
    ciphertext = encrypt(string, shift)
    print("Encrypted String:", ciphertext)
    plaintext = decrypt(ciphertext, shift)
    print("Decrypted String:", plaintext)

