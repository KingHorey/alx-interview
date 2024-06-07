#!/usr/bin/python3
"""interview question module
locked boxes
"""


def canUnlockAll(boxes):
    """check if all boxes can be unlocked"""
    valid = []
    lent = len(boxes)
    for n in range(lent):
        valid.append("locked")
    valid[0] = "unlocked"
    status = False
    for i in range(len(valid)):
        if status is True:
            break
        else:
            status = True
        for check in range(len(valid)):
            if valid[check] == "locked":
                status = False
            if valid[check] == "unlocked":
                getkey = boxes[check]
            for i in getkey:
                if i < lent:
                    valid[i] = "unlocked"
    for validate in valid:
        if validate == "locked":
            return (False)
    return (True)
