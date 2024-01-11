#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Function that determines if all the locked boxes can be opened.

    Parameters:
    - boxes: A list of lists representing locked boxes and their corresponding keys.

    Returns:
    - True if all boxes can be opened, False otherwise.
    """

    # Check if input is a list
    if type(boxes) is not list:
        return False

    # Check if the list is empty
    elif len(boxes) == 0:
        return False

    # Iterate through the keys to check if they can open the corresponding boxes
    for key in range(1, len(boxes) - 1):
        boxes_checked = False

        # Iterate through the boxes
        for idx in range(len(boxes)):
            # Check if the key can open the box and the key is not the same as the box index
            boxes_checked = key in boxes[idx] and key != idx

            # If the key can open the box, exit the inner loop
            if boxes_checked:
                break

        # If a key cannot open any box, return False
        if not boxes_checked:
            return False

    # If all keys can open corresponding boxes, return True
    return True
