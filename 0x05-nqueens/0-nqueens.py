#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line,
and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
"""

import sys


def create_positions(n: int) -> list:
    """returns a list of possible positions"""
    possibles = []
    for i in range(n):
        for j in range(n):
            possibles.append([i, j])
    return possibles


def cancel_VH(complete_list: list, post: list):
    """
    returns a new list with vertical and diagonal
    position canceled out
    """
    new_list = []
    for values in complete_list:
        if values[0] != post[0] and values[1] != post[1]:
            new_list.append(values)
    return new_list


def cancel_diag(full_list: list, post: list) -> list:
    """
    returns a new list with diagonals
    removed left right up down
    """
    new_list = []
    list2 = []
    for elements in full_list:
        diff = post[0] - elements[0]
        if post[1] - diff != elements[1]:
            new_list.append(elements)
    for elements in new_list:
        diff = post[0] - elements[0]
        if post[1] + diff != elements[1]:
            list2.append(elements)
    return list2


def remove_invalid(lst: list, pos: list):
    """returns a new list valid for other queens to stand"""
    vhout = cancel_VH(lst, pos)
    diagout = cancel_diag(vhout, pos)
    return diagout


def visual(pos, num):
    """prints postion in a visible manner"""
    z = 0
    for indexes in range(num):
        for y in range(num):
            try:
                if indexes == pos[z][0] and y == pos[z][1]:
                    print(f"{pos[z]} ", end="")
                    z += 1
                else:
                    print("[x, x] ", end="")
            except IndexError:
                print("[x, x] ", end="")
        print()


def arrange_queens(possible: list, num: int):
    """returns all posible poitions of queens
       without taking each other out"""
    grand_list = []
    trash = possible.copy()
    for y in range(num):
        sub_list = []
        for elements in range(num):
            print(f"chcking out {[elements, y]} in {trash}")
            if [elements, y] in trash:
                print(f"found {[elements, y]}")
                sub_list.append([elements, y])
                trash = remove_invalid(trash, [elements, y])
                visual(trash, num)
        grand_list.append(sub_list)
    return grand_list


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nums = int(sys.argv[1])
        if nums < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    hor = 0
    ver = 0
    grand = []
    pointer = []
    sub = []
    invalids = []
    while hor < nums:
        for i in range(nums):
            pointer.append([i, hor])
        # print(pointer)
        possibles = create_positions(nums)
        for xy in range(len(sub)):
            possibles = remove_invalid(possibles, sub[xy])
        visual(possibles, nums)
        x = len(sub)
        if x < 0:
            x = 0
        while x < nums:
            print(f"checking for {pointer[x]} in {possibles} and {invalids}")
            if pointer[x] in possibles and pointer[x] not in invalids:
                sub.append(pointer[x].copy())
                possibles = remove_invalid(possibles, pointer[x])
                print(f"found {pointer[x]}")
                visual(possibles, nums)
                x += 1
                ver = 0
            else:
                if ver < nums:
                    if pointer[x][1] == nums - 1:
                        pointer[x][1] = 0
                    else:
                        pointer[x][1] += 1
                    print(f"new {pointer[x]}")
                    ver += 1
                else:
                    print(f"found none at {x}")
                    ver = 0
                    break
        print(sub)
        if len(sub) == nums:
            grand.append(sub)
            hor += 1
            pointer = []
            sub = []
            invalids = []
        elif len(sub) == 1:
            hor += 1
            pointer = []
            sub = []
            invalids = []
            # break
        else:
            invalids.append(sub.pop())
            ver = 0
            print(sub)
        print("-----------------------------------------------------")
    for each in grand:
        print(each)
