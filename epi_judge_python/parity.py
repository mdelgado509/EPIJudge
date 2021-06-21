"""Returns the parity of a 64 bit integer x"""
from test_framework import generic_test


def parity(x: int) -> int:
    """
    Parity is 1 when number of set bits are odd,
        0 when number of set bits are even

    This is a brute force algorithm that iterates over each bit, tests each bit,
        and tracks whether the number of 1s seen so far is odd or even

    The time complexity is `O(n)` where n is the number of bits in the int input
    """
    # keeps track of parity
    parity_result = 0
    # iterates each bit until x is 0
    while x:
        # x & 1 checks if the first bit is set? (returns 1 if set 0 if not)
        # XOR: a & b
        #      0 ^ 0 == 0
        #      1 ^ 0 == 1
        #      0 ^ 1 == 0
        #      1 ^ 1 == 0
        parity_result ^= x & 1
        # right shift to reveal the next least significant bit
        x >>= 1
    # return parity result
    return parity_result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
