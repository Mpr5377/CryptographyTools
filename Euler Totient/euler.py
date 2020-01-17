"""
Name: Matt Robinson
Filename: euler.py
Description: Visualization of how the euler totient function works
Language: Python 3
"""
import math


def factor(number):
    factors = set()
    if number < 5:
        for i in range(2,int((number//2)+1)):
            while number % i == 0:
                number /= i
                factors.add(i)
    else:
        for i in range(2, int(number//2)):
            while number % i == 0:
                number /= i
                factors.add(i)
    return factors


def totient(number, set):
    if len(set) == 0:
        print("Total:", number-1)
        return number - 1
    total = number
    for i in set:
        total *= (1 - (1/i))
    print("Total:", int(total))
    return total


if __name__ == "__main__":
    number = 113
    totient(number, factor(number))