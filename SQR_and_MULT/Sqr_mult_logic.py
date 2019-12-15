"""
File: Sqr_mult_logic
Name: Matt Robinson
Description: This file is going to just be a test to see if I can successful write a program to do SQR and MULT for me
Language: Python
"""


def square_and_multiply(base, exponent, modulo):
    """
    Function: square_and_multiply
    Description: The main logic for the Square and Multiply Algorithm. Prints out the final value to the console
    :param base: The base of the number
    :param exponent: The exponent that the base is raised to
    :param modulo: The modulo for reduction
    :return: None
    """
    binary_exponent = convert_to_binary(exponent)
    value = base
    # 1 - Square and Multiply
    # 0 - Square only
    for step in binary_exponent:
        if step == '1':
            value = multiply(square(value), base)
        else:
            value = square(value)
        value = value % modulo
    print(value)


def convert_to_binary(exponent):
    """
    Function: convert_to_binary
    Description: Takes in a number and returns its binary representation
    :param exponent: The number to be converted to binary
    :return: The binary representation of the exponent parameter
    """
    binary = bin(exponent).split("b")[1][1:]
    return binary


def square(number):
    """
    Function: square
    Description: Takes in a number and squares it
    :param number: The number to be squared
    :return: The result of squaring the number parameter
    """
    return number**2


def multiply(value, base):
    """
    Function: multiply
    Description: Multiplies the current value by the base number
    :param value: The current value of the number at the given step
    :param base: The original base for the number
    :return: The result of value multiplied by base
    """
    return value * base


if __name__ == '__main__':
    square_and_multiply(12345, 6789, 143)



