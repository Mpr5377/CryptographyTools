"""
Name: Matt Robinson
Professor: Michael Kurdziel
Class: Introduction to Cryptography
Assignment: Homework #10
"""
import random


def miller_rabin(num, a):
    """
    Function: miller_rabin
    Description: Returns True if the parameter "num" is a prime number, otherwise returns false
    Params: num: Odd number to be tested
            a: Random Base number
    Returns: True - num is prime
             False - num is composite
    """
    s = num - 1
    k = 0
    # While s is even, divide by 2, keep track of number of times s has been halved with k
    while s % 2 == 0:
        s = s // 2
        k += 1

    # Miller-Rabin algorithm
    # Raise a^s and store as b, then mod it with num
    b = pow(a, s, num)
    # Derived from sudo-code on wikipedia at https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
    if b != 1 and b != num - 1:
        j = 1
        while j < k and b != (num - 1):
            b = (b ** 2) % num
            if b == 1:
                # Composite Number
                return False
            j += 1
        if b != num - 1:
            # Composite Number
            return False
    # Prime Number
    return True


def get_errors(errors):
    """
    Function: get_errors(errors)
    Description: Prints out the Error information to the console
    Params: errors: dictionary containing integers and their error probability
    :return: None
    """
    # Get the largest error probability value
    largest_error = max(list(errors.values()))
    # Get the Integer for the largest probability value
    largest_int = list(errors.keys())[list(errors.values()).index(largest_error)]
    # Print the largest error value
    print("Largest error:")
    print("+--------+----------+")
    print("| " + str(largest_int) + " | " + "{:.6f}".format(largest_error) + " |")
    print("+--------+----------+\n")
    print("10 Largest:")
    # Get the Top 10 Highest Error Integers and store them in top_error_list
    top_error_list = sorted(errors, key=errors.get, reverse=True)[:10]
    # Print the next top 10 integers with the highest error probability value
    for x in top_error_list:
        # print: [<int>] -> <error probability>
        print("+--------+----------+")
        print("| " + str(x) + " | " + "{:.6f}".format(errors[x]) + " |")
    print("+--------+----------+")


def get_range(start, finish):
    """
    Function: get_range()
    Description: Get all odd numbers and run Miller_Rabin Algo on them
    Params: start: The start of the range to be checked
            finish: The end of the range to be checked
    :return: None
    """
    # Get all odd numbers in defined range
    odd_list = []
    for x in range(start, finish):
        if x % 2 == 1:
            odd_list.append(x)
    # dict to hold our error probabilities
    errors = {}
    # Loop through and check each number
    for num in odd_list:
        # count of truths and fallacies
        true_count = 0
        # try to falsify primalities 20 times
        for x in range(20):
            # Random base
            a = random.randint(2, num - 1)
            r = miller_rabin(num, a)
            if r:
                true_count += 1
        # if neither are equal to zero it means there are false positives
        if true_count != 0 and true_count != 20:
            errors[num] = float(true_count) / 20.0
    get_errors(errors)


if __name__ == '__main__':
    get_range(105000, 115000)