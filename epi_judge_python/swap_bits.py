"""Takes a 64-bit integer and swaps the bits at indices i and j"""
from test_framework import generic_test


def swap_bits(x, i, j):
    """Takes a 64-bit integer and swaps the bits at indices i and j"""
    # Extract the i-th annd j-th bit by bitwise right shifting
    # with a value of i and j repectively and return that value
    # by bitwise & with 1
    # Compare the values to check if they are different
    if (x >> i) & 1 != (x >> j) & 1:
        # set a bit mask by setting bits at indices i and j through left
        # shifting 1 by the respective values and taking the bitwise
        # OR result
        bit_mask = (1 << i) | (1 << j)
        # XOR x and bit_mask to switch bits at indices i and j
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
