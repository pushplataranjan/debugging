"""Demo code for breakpoint commands"""

import sys

def fibonacci(number):
	""" return the nth fibonacci number """
	number = int(number)
	if number <= 1:
		return 1

	return fibonacci(number-1)+fibonacci(number-2)


if __name__ == '__main__':
	import pdb; pdb.set_trace()
	print (sys.argv[-1])
	print (fibonacci(sys.argv[-1]))