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
    triangle = []  # Initialize an empty list to store Pascal's Triangle
    
    if n <= 0:
        return triangle  # Return an empty list if n is less than or equal to 0
    
    triangle = [[1]]  # Initialize the triangle with the first row containing 1
    
    for i in range(1, n):  # Loop to generate subsequent rows of the triangle
        temp = [1]  # Initialize the row with the first element as 1
        for j in range(len(triangle[i - 1]) - 1):
            # Calculate each element of the row based on the previous row
            temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        temp.append(1)  # Append the last element as 1 to complete the row
        triangle.append(temp)  # Add the row to the triangle
    
    return triangle  # Return the generated Pascal's Triangle
