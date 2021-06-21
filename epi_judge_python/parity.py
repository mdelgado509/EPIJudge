"""Returns the parity of a 64 bit integer x"""
from test_framework import generic_test


def parity(x: int) -> int:
    """
    Parity is 1 when number of set bits are odd,
        0 when number of set bits are even
    """
    # keeps track of parity
    result = 0

    # This is an improvement on the brute force approach where the time
    # complexity is reduced to `O(n)` where n is the number of SET bits of int
    #
    # This algorithm exploits the bit fiddling trick:
    # x &= (x - 1) which removes the last set bit
    # e.g. 0b0101000 & 0b0100111 == 0b0100000
    #
    # iterates through each SET bit
    while x:
        # x is nonzero so we flip the parity each time
        # flipping parity each iteration instead of flipping only when finding
        # a set bit in the last significant bit
        result ^= 1
        # removes last set bit
        x &= (x - 1)
    return result

    # This is a brute force algorithm that iterates over each bit, tests each bit,
    # and tracks whether the number of 1s seen so far is odd or even
    #
    # The time complexity is `O(n)` where n is the number of bits in the int input
    #
    # iterates each bit until x is 0
    while x:
        # x & 1 checks if the first bit is set? (returns 1 if set 0 if not)
        # XOR: a & b
        #      0 ^ 0 == 0
        #      1 ^ 0 == 1
        #      0 ^ 1 == 0
        #      1 ^ 1 == 0
        #
        # this flips the parity when a set bit is found in the last significant
        # bit position
        result ^= x & 1
        # right shift to reveal the next least significant bit
        x >>= 1
    # return parity result
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
