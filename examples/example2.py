"""Demo code for post-mortem mode """

import sys


def divide_operation(numerator, denominator):

    return numerator / denominator


if __name__ == '__main__':
    """ get numerator and demoninator value and print divide result"""
    numerator = int(sys.argv[1])
    denominator = int(sys.argv[2])
    try:
        result =divide_operation(numerator, denominator)
    except:
        import pdb;pdb.post_mortem()