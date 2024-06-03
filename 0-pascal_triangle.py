#!/usr/bin/python3

def pascal_triangle(n):
    """ function to get pascals triangle using recursion"""
    if n <= 0 or type(n) is not int:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        data = []
        i = 1
        while i <= n:
            if i <= 2:
                result = pascal_triangle(i)
            else:
                result = my_function(result, i)
            data.append(result)
            i += 1
    return data


def my_function(data, count):
    """ sub function to get the pascal triangle when count is greater than 2"""
    new_list = []
    i = 0
    while i < count:
        if (i == 0 or i == count - 1):
            new_list.append(1)
        else:
            new_list.append(data[i] + data[i - 1])
        i += 1
    return new_list
