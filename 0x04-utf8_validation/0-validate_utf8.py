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
        if data[index] & 0b10000000 == 0b00000000:
            index += 1
            continue
        elif data[index] & 0b11100000 == 0b11000000:
            count = 2
        elif data[index] & 0b11110000 == 0b11100000:
            count = 3
        elif data[index] & 0b11111000 == 0b11110000:
            count = 4
        else:
            return False

        # check if there are sufficient bits to look for in the array

        # index += 1
        for _ in range(1, count):
            try:
                if (_ >= len(data) or data[_ + index] & 0b11000000 !=:

                        0b10000000):
                    return False
            except IndexError:
                return False
        index += count
    return True
