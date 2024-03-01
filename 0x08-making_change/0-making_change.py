#!/usr/bin/python3
""" Coin Change Algorithm """

def makeChange(coins, total):
    """ Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to achieve the total. Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any combination of coins.

    Note:
        - coins is a list of the values of the coins in your possession.
        - The value of a coin will always be an integer greater than 0.
        - You can assume you have an infinite number of each denomination of coin in the list.
        - Your solution’s runtime will be evaluated in this task.
    """
    if total <= 0:
        return 0

    check = 0
    temp = 0
    coins.sort(reverse=True)

    for i in coins:
        while check < total:
            check += i
            temp += 1

        if check == total:
            return temp

        check -= i
        temp -= 1

    return -1