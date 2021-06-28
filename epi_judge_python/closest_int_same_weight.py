from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    """
    Finds the closest 64 bit int with the same bit weight
    """
    # Another approach to isolating the bits and creating the bit mask
    # this apporach is O(1)
    # isolate LSB
    # 11011010 - 1 = ~11011001 = 00100110 & 11011010 = 00000010
    lowest_set_bit = x & ~(x - 1)
    if lowest_set_bit & 1: # if loweset set bit is 1st bit
        # sets next unset bit
        lowest_set_bit = (~x & ~(~x - 1))
    # create a bit mask with LSB (or 2nd LSB) and next unset bit
    bit_mask = lowest_set_bit | (lowest_set_bit >> 1)
    # XOR x with bit_mask to flip LSB (or 2nd LSB) and the next unset bit
    return x ^ bit_mask
    #
    # This book solution is O(n) where n is number of bits
    # total possible num bits
    num_bits = 64
    # iterates through indices 0 to 63
    for i in range(num_bits - 1):
        # right shift to each bit at indices i and i + 1
        # if num[i] num[i + 1] aren't equal execute code block
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            # to flip the bits at indices i and i + 1
            # create a bit mask
            # left shift by i and i + 1 and OR the result
            # XOR with x to flip bits at i and i + 1
            x ^= (1 << i) | (1 << (i + 1))
            return x

    # Raise error if all bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
