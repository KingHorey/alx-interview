#!/usr/bin/python3
"""
no modules imported
"""


def minOperations(n):
    """find minimum operation"""
    from math import sqrt
    if n <= 1:
        return 0

    def is_prime(number):
        """checks for prime numbers"""
        if number == 2:
            return True
        sq_num = int(sqrt(number)) + 1
        if number % 2 == 0 or number % sq_num == 0:
            return False
        for i in range(2, sq_num):
            if number % i == 0:
                return False
        return True

    if is_prime(n):
        return n
    min_op = []
    div = 2
    while n > 1:
        if is_prime(div):
            if n % div == 0:
                min_op.append(div)
                n = n / div
            else:
                div = div + 1
        else:
            div = div + 1
    return sum(min_op)
