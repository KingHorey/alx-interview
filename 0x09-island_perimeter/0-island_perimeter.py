#!/usr/bin/python3
"""Calcluate the perimeter of an Island"""


def island_perimeter(grid):
    """Calculate the perimeter of an island"""
    row = 0
    column = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == 0:
                if grid[i][j] == 1:
                    # print(f'adding from zero end {i}, {j}')
                    row += 1
            elif j == len(grid[i]) - 1:
                if grid[i][j] == 1:
                    row += 1
                elif grid[i][j] != grid[i][j - 1]:
                    row += 1
                    # print(f'adding from last end {i}, {j}')
            else:
                if grid[i][j] != grid[i][j - 1]:
                    row += 1
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            # print(j, i)
            if j == 0:
                if grid[j][i] == 1:
                    column += 1
            elif j == len(grid) - 1:
                if grid[j][i] == 1:
                    column += 1
                elif grid[j][i] != grid[j - 1][i]:
                    column += 1
            else:
                if grid[j][i] != grid[j - 1][i]:
                    column += 1
    return row + column
