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
        elif data[index] & 0b11 == 0b110:
            count = 2
        elif data[index] & 0b111 == 0b111:
            count = 3
        elif data[index] & 0b1111 == 0b11110:
            count = 4
        else:
            return False

        # index += 1
        for _ in range(1, count):
            if data[_] >> 6 != 0b10:
                return False
        index += count
    return True


# data = [467, 133, 108]
# print(validUTF8(data))