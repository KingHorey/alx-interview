#!/usr/bin/env python

""" import annotation assistants """
from typing import List


def validUTF8(data: List) -> bool:
	""" validate utf8 """
	if not isinstance(data, list):
		return False
	if not data:
		return False

	count = 0
	index = 0

	#  get the number of bytes for the first index
	if data[index] >> 7 == 0b0 or len(data) == 1:
		return True
	elif data[index] >> 3 == 0b1111:
		count = 4
	elif data[index] >> 4 == 0b1110:
		count = 3
	elif data[index] >> 5 == 0b110:
		count = 2
	elif data[index] >> 7 == 0b1:
		count = 1

	return check_sequence(count, data)


def check_sequence(count: int, dt: List) -> bool:
	""" check if sequence is valid """
	index = 1
	try:
		for i in range(count):
			if dt[index + i] >> 6 == 0b10:
				continue
			else:
				return False
	except IndexError:
		pass
