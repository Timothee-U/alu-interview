#!/usr/bin/python3
"""
0-rain.py

Module that provides a function to calculate the total amount of rainwater
retained between walls represented as a list of non-negative integers.

The walls list represents a cross-section of a terrain where each element
is the height of a wall with unit width. After raining, water may be trapped
between the walls depending on their heights.

Example:
    >>> rain([0, 1, 0, 2, 0, 3, 0, 4])
    6
"""


def rain(walls):
    """
    Calculate the total units of rainwater retained after raining.

    The function uses the two-pointer concept with precomputed maximum heights:
    - left_max[i] is the highest wall from the left up to index i.
    - right_max[i] is the highest wall from the right up to index i.
    Water trapped at index i is the minimum of left_max[i] and right_max[i]
    minus the height of the wall at that index.

    Args:
        walls (list of int): List of non-negative integers representing wall
                             heights. An empty list returns 0.

    Returns:
        int: Total units of water retained between the walls.

    Algorithm steps:
        1. Handle empty list case by returning 0.
        2. Initialize two lists:
           - left_max: stores the max wall height to the left of each index.
           - right_max: stores the max wall height to the right of each index.
        3. Fill left_max by iterating from left to right.
        4. Fill right_max by iterating from right to left.
        5. Calculate water trapped at each index:
           water += min(left_max[i], right_max[i]) - walls[i]
        6. Return the total water accumulated.

    Example usage:
        >>> walls = [2, 0, 0, 4, 0, 0, 1, 0]
        >>> rain(walls)
        10
    """
    if not walls:
        return 0

    length = len(walls)
    water = 0

    # Initialize arrays to store max heights to the left and right
    left_max = [0] * length
    right_max = [0] * length

    # Compute left_max values
    left_max[0] = walls[0]
    for i in range(1, length):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Compute right_max values
    right_max[-1] = walls[-1]
    for i in range(length - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water trapped at each index
    for i in range(length):
        trapped = min(left_max[i], right_max[i]) - walls[i]
        water += trapped

    return water
