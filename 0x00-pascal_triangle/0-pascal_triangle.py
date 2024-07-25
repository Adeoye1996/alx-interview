#!/usr/bin/python3

"""
Module for generating Pascal's triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row of the triangle
    for _ in range(1, n):
        # Previous row padded with zeros at both ends
        previous_row = [0] + triangle[-1] + [0]
        # Calculate the new row using the sum of adjacent elements
        new_row = [previous_row[i] + previous_row[i + 1] for i in range(len(previous_row) - 1)]
        # Append the new row to the triangle
        triangle.append(new_row)
    
    return triangle
