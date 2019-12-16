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
    print("Base: ", base)
    print("Exponent: ", exponent)
    print("Modulo: ", modulo)
    binary_exponent = convert_to_binary(exponent)
    print("Exponent to Binary: ", "1" + str(binary_exponent))
    value = base
    step_counter = 2
    # 1 - Square and Multiply
    # 0 - Square only
    print("+----------+----------+------------------------+------------------------+")
    print("|   Step   |  Binary  |          SQR           |           MULT         |")
    print("+----------+----------+------------------------+------------------------+")
    print("\t 1\t\t\t1\t\t\t\t  -\t\t\t\t\t\t  " + str(base))

    for step in binary_exponent:
        if step == '1':
            v = value
            sqr = square(value) % modulo
            value = multiply(sqr, base) % modulo
            print("\t " + str(step_counter) + "\t\t\t1\t\t" + str(v) + "^2 mod " + str(modulo) + " = " + str(sqr), "\t\t(" + str(sqr) + " * " + str(base) + ") mod " + str(modulo) + " = " + str(value))
        else:
            v = value
            value = square(value) % modulo
            print("\t " + str(step_counter) + "\t\t\t0\t\t" + str(v) + "^2 mod " + str(modulo) + " = " + str(value) + "\t\t\t\t    -")
        step_counter += 1
    print("\nFinal Value: " + str(value))


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
    square_and_multiply(37, 39, 730)
