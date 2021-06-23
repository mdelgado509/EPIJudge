"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned
integer consisting of bits of the input in reverse order.
"""
from test_framework import generic_test

def populate_reverse_bits(x: int) -> int:
    """
    This is the brute force solution to reversing a 64-bit input by bits
    """
    # set size to bit length of input
    # in this case we want to populate a 16-bite precomputed cache
    size = 16
    # the position variable keeps track of the MSB -> LSB index of the output
    # reversed bit order binary number
    position = size - 1
    # the result is OR
    result = 0
    while position >= 0:
        result |= ((x & 1) << position)
        x >>= 1
        position -= 1
    return result

LOOKUP = {}

for i in range(1 << 16):
    LOOKUP[i] = populate_reverse_bits(i)

def reverse_bits(x: int) -> int:
    """
    This program takes a 64-bit int as an input and returns an output
    of the int bits in reverse order
    """
    # This function uses a cache to reverse 16 bit segments of a 64-bit int
    # HINT: do not create a build function as the program will have to
    # build the cache for each test case
    #
    # Instead just loop through the cache and fill in global scope as done above
    mask_size = 16
    bit_mask = 0xFFFF
    return (LOOKUP[x & bit_mask] << (3 * mask_size) | # extract last 16 bits reverse and left shift 48 OR with
            LOOKUP[(x >> mask_size) & bit_mask] << (2 * mask_size) | # extract 2nd to last 16 bits left shift 32 OR with
            LOOKUP[(x >> (2 * mask_size)) & bit_mask] << mask_size | # extract 3rd to last 16 bits left shift 16 OR with
            LOOKUP[(x >> (3 * mask_size)) & bit_mask]) # extract 1st 16 bits
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
