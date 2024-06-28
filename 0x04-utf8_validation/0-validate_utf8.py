#!/usr/bin/python3

""" no modules imported """


def validUTF8(data):
    """ validate utf-8 sequence """
    if not isinstance(data, list):
        return False
    index = 0
    while index < len(data):  # in the case of nested lists
        if data[index] < 0:
            return False
        if data[index] >> 7 == 0b0:
            return True
        elif data[index] & 0b11100000 == 0b11000000:
            count = 2
        elif data[index] & 0b11110000 == 0b11100000:
            count = 3
        elif data[index] & 0b11111000 == 0b11110000:
            count = 4
        else:
            return False

        # index += 1
        for _ in range(1, count):
            if data[_] >> 6 != 0b10:
                return False
        index += count
    return True
