"""Demo code for set_trace mode"""

import sys
import pdb


def divide_operation(numerator, denominator):
	print ("Starting set_trace mode")
	pdb.set_trace()
	print ("Print first line under trace mode")
    return numerator / denominator


if __name__ == '__main__':
    """ get numerator and demoninator value and print divide result"""
    numerator = int(sys.argv[1])
    denominator = int(sys.argv[2])
    divide_operation(numerator, denominator)