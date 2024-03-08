#!/usr/bin/python3
"""Module for computing the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """Calculates the perimeter of an island in a 2D grid.

    Args:
        grid (list): A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    # Check if input is a list
    if type(grid) != list:
        return 0

    # Iterate through each cell in the grid
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue

            # Check neighboring cells to determine edges
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            
            # Update perimeter based on edges
            perimeter += sum(edges)
    return perimeter
