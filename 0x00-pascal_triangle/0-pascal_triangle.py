#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    Args:
    - n (int): The number of rows for Pascal's Triangle
    
    Returns:
    - list: A list of lists representing Pascal's Triangle up to the nth row.
            Returns an empty list if n is less than or equal to 0.
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
