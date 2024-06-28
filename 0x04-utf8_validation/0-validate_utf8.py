#!/usr/bin/python


def validUTF8(data):
    if not isinstance(data, list):
        return False
    index = 0
    count = 0
    while index < len(data):  # in the case of nested lists
        if data[index] >> 7 == 0b0:
            count = 1
        elif data[index] >> 5 == 0b110:
            count = 2
        elif data[index] >> 4 == 0b1110:
            count = 3
        elif data[index] >> 3 == 0b11110:
            count = 4
        else:
            return False
        index += 1
        for _ in range(index, count):
            if data[_] >> 6 == 0b10:
                pass
            else:
                return False
    return True
