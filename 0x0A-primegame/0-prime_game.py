#!/usr/bin/python3
"""
Module defining the isWinner function.

This module contains functions related to determining the winner in a prime game.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of each round of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        maria_turn = True
        for i in range(2, num + 1):
            if is_prime(i):
                if maria_turn:
                    maria_wins += 1
                else:
                    ben_wins += 1
                maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

