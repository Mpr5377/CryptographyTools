"""
File: Birhtday_Paradox.py
Name: Matt Robinson
Description: This function displays the probability of a collision based on the birthday paradox.
Language: Python
"""


def birthday_paradox(start, end):
    """
    Function: birthday_paradox
    Description: Given a start and an end parameter, calculates the probability of a collision for all values in that
                 range
    :param start: The starting number of the range
    :param end:  The ending number of the range
    :return: None
    """
    t = start
    while t <= end:
        total = 1
        for i in range(1, t):
            total = total * (1 - (i / 365))

        # modify '1 - total' to total, if you want to see the probability that there wont be a collision
        print("Probability of a collision for " + str(t) + " people: " + str(1 - total))
        t += 1


if __name__ == '__main__':
    birthday_paradox(15, 30)
