#!/usr/bin/python3
""" Python script for generating change """

def make_change(coins, total):
    """ Generate the minimum number of coins needed to reach a total amount.

    Args:
        coins (list): List of available coin denominations.
        total (int): Total amount needed.

    Returns:
        int: Minimum number of coins needed, or -1 if it's not possible to reach the total.
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

