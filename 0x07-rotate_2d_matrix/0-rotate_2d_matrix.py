#!/usr/bin/python3
"""
Module: 2D Matrix Rotation

This module provides a function for in-place 90-degree rotation of a 2D matrix.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix in place.

    Parameters:
    - matrix (list of lists): The 2D matrix to be rotated.

    Notes:
    - The function performs the rotation in an in-place manner.
    - If the input is not a valid 2D matrix, the function exits without rotation.

    Algorithm:
    - Initialize pointers c and r for matrix rotation.
    - Iterate through each element in the matrix:
        - Check if a new row needs to be created in the rotated matrix.
        - Add the rotated element to the new row.
        - Check if the original row is completed, and remove it.
        - Update pointers for the next iteration.
    """
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if any(len(row) != cols for row in matrix):
        return

    # Initialize pointers for matrix rotation
    c, r = 0, rows - 1

    # Iterate through each element in the matrix
    for i in range(cols * rows):
        # Check if a new row needs to be created in the rotated matrix
        if i % rows == 0:
            matrix.append([])

        # Add the rotated element to the new row
        matrix[-1].append(matrix[r][c])

        # Check if the original row is completed, and remove it
        if c == cols - 1 and r >= -1:
            matrix.pop(r)

        # Update pointers for the next iteration
        r -= 1
        if r == -1:
            r = rows - 1
            c += 1
