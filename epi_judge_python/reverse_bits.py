"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned
integer consisting of bits of the input in reverse order.
"""
from test_framework import generic_test

def reverse_bits(x: int) -> int:
    """
    This program takes a 64-bit int as an input and returns an output
    of the int bits in reverse order
    """
    #
    # This function reverses the bits of the input and returns an output in
    # reverse order. The size is set to the int bit length.
    #
    # O(n) time complexity where n is the size of the int in bits
    #
    # int bit length
    size = 64
    # position of where each reversed bit will go (starting at 0 to 63 for a
    # 64-bit integer)
    position = size - 1
    # the return value
    result = 0
    # iterate over each reversed bit position
    while position >= 0:
        # x & 1 isolates the LSB
        # << position places that bit in a position bit mask
        # bitwise OR with the result until the entire number is reversed by bits
        result |= ((x & 1) << position)
        # right shift x to expose the next LSB
        x >>= 1
        # decrement the positon to set the next value to the next reversed bit
        # position in the resulting output
        position -= 1
    return result





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
