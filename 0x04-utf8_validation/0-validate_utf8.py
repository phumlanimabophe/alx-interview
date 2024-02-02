#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 encoding or not.

    Args:
        data (list): A list of integers representing a data set.

    Returns:
        bool: True if the data set is a valid UTF-8 encoding, else False.
    """
    count = 0  # Number of expected continuation bytes for the current character

    for d in data:
        if count == 0:
            # Check if the current byte is a start byte
            if d & 0b10000000 == 0:
                count = 0
            elif d & 0b11100000 == 0b11000000:
                count = 1
            elif d & 0b11110000 == 0b11100000:
                count = 2
            elif d & 0b11111000 == 0b11110000:
                count = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if d & 0b11000000 != 0b10000000:
                return False
            count -= 1

    # Check if there are no remaining incomplete characters
    return count == 0

