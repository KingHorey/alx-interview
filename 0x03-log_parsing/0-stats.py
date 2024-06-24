#!/usr/bin/python3

""" parse logs on stdin """

import sys
import re
import signal

sys_inputs = sys.stdin
lines_count = 0
rounds = 0
file_size = 0
status_codes = {}
converted = False
converted_code = False
valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
valid_code = False


def print_result(codes=None) -> None:
    print("File size: {}".format(file_size))
    if codes:
        for key, value in sorted(codes.items()):
            print("{}: {}".format(key, value))


def signal_handler(sign, frame):
    print_result(status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

input_list = sys_inputs.readlines()
input_size = len(input_list)

if input_size == 0:
    print_result()

for i in range(input_size):
    sys_input = input_list[i].strip()
    lines_count += 1
    rounds += 1
    """ check with regex if the input matches pattern """
    regex_check = re.match(r'(.*?).?-.?\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{'
                           r'2}.\d{6}] .*? ([\\d\w]*?) (\d*)?', sys_input)
    if regex_check:
        """ if the input matches the pattern, extract the status code
        and the file size """
        code, size = regex_check.group(2, 3)
        try:
            code = int(code)  # convert to int
            converted_code = True
            if code in valid_codes:
                valid_code = True
                try:
                    file_size += int(size)
                    converted = True
                    if converted and converted_code:
                        if code in status_codes:
                            status_codes[code] += 1
                        else:
                            status_codes[code] = 1
                        valid_code = False
                except TypeError:
                    continue
            else:
                continue
        except ValueError:
            try:
                new_size = int(size)
                file_size += new_size
            except ValueError:
                continue
    if lines_count == 10:
        print_result(status_codes)
        lines_count = 0

    if lines_count != 10 and i == input_size - 1:
        print_result(status_codes)

    elif not regex_check:
        continue
