#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime
import fileinput

with fileinput.input(files=('inputs.txt')) as f_input:
    for line in f_input:
        sleep(random.random())
        sys.stdout.write(line)
        sys.stdout.flush()

# for i in range(10000):
#     sleep(random.random())
#     sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
#         random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
#         datetime.datetime.now(),
#         random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
#         random.randint(1, 1024)
#     ))
#     sys.stdout.flush()


