#!/usr/bin/python3
"""A module that rotates 2D matrix clockwise"""


def rotate_2d_matrix(matrix):
    """A function that rotates a 2D matrix"""
    length = len(matrix)
    temp = matrix.copy()
    for row in range(length - 1, -1, -1):
        replace = []
        for column in range(length - 1, -1, -1):
            replace.append(temp[column][row])
        matrix[row] = replace
