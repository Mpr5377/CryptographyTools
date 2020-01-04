"""
Name: Matt Robinson
Filename: caesar.py
Description: Demonstrating a caesar cipher's encrypt and decryption functions
Language: Python
"""
def encrypt(plaintext, shift):
    """
    Function: encrypt
    Description: Given plaintext encrypt it with the provided shift and return the ciphertext
    :param plaintext: The text to be encrypted
    :param shift: The shift to be used for the encryption
    :return: The encrypted string
    """
    encrypted_string = ""
    for c in plaintext:
        encrypted_string += chr(ord(c) + shift % 26)
    print("Encrypted String:", encrypted_string)
    return encrypted_string


def decrypt(ciphertext, shift):
    """
    Function: decrypt
    Description: Given ciphertext decrypt it with the provided shift and return the plaintext
    :param ciphertext: The encrypted text to be decrypted
    :param shift: The shift to be used for the decryption
    :return: The decrypted string
    """
    decrypted_string = ""
    for c in ciphertext:
        decrypted_string += chr(ord(c) - shift % 26)
    print("Decrypted String:", decrypted_string)
    return decrypted_string


def decrypt_brute_force(ciphertext):
    """
    Function: decrypt_brute_force
    Description: Brute force the decryption of a given ciphertext
    :param ciphertext: The ciphertext to be decrypted
    :return: The plaintext that was decrypted
    """
    print(ciphertext)
    for shift in range(1,26):
        decrypted_string = ""
        for c in ciphertext:
            decrypted_string += chr(ord(c) - shift % 26)
        print("Shift of " + str(shift) + ": ", decrypted_string)


if __name__ == '__main__':
    # Insert the string to be encrypted or decrypted
    string = ""
    # Insert the shift to be used for encryption or decryption
    shift = 0

