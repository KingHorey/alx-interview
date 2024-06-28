#!/usr/bin/python3

""" no modules imported """


def validUTF8(data):
    """ validate utf-8 sequence """
    if not isinstance(data, list):
        return False
    index = 0
    while index < len(data):  # in the case of nested lists
        if data[index] > 255 or data[index] < 0:
            return False
        if data[index] >> 7 == 0b0:
            # count = 1
            return True
        elif data[index] >> 5 == 0b110:
            count = 2
        elif data[index] >> 4 == 0b1110:
            count = 3
        elif data[index] >> 3 == 0b11110:
            count = 4
        else:
            return False

        for _ in range(1, count):
            if data[index + _] >> 6 != 0b10:
                return False
        index += count
    return True
