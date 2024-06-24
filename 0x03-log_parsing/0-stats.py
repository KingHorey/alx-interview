#!/usr/bin/python3

""" parse logs on stdin """

import sys
import re

sys_inputs = sys.stdin
lines_count = 0
file_size = 0
status_codes = {}
for sys_input in sys_inputs:
    sys_input = sys_input.strip()
    lines_count += 1
    """ check with regex if the input matches pattern """
    regex_check = re.match(r'(.*?) - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{'
                           r'2}.\d{6}] .*? (\d*?) (\d*)?', sys_input)
    if regex_check:
        """ if the input matches the pattern, extract the status code
        and the file size """
        code, size = regex_check.group(2, 3)
        file_size += int(size)
        code = int(code)
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1
    if lines_count == 10:
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            print("{}: {}".format(key, value))
        lines_count = 0
    elif not regex_check:
        continue
