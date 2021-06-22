"""Returns the parity of a 64 bit integer x"""
from test_framework import generic_test

# To fully explain the 3rd method, which in practice is better because you
# are performing fewer bitwise operations compared to version 4
#
# First we are going to create a populate_parity function that will be
# used to populate our parity lookup table
def populate_parity(x: int) -> int:
    """
    This function populates a parity lookup table
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

# Then we define our lookup table as an empty dictionary
LOOKUP = {}
# if we were to do a 64-bit lookup table this would be a memory and time
# intensive process for i in range(1 << 64) [from 1 to 64 bit space]
#
# instead we can use a 16-bit lookup table and check each 16 bit section
# of the 64-bit integer
for i in range(1 << 16):
    # i is the bin set to the key and the parity of i is the value
    LOOKUP[i] = populate_parity(i)

# Now we can define our parity function and exploit our LOOKUP table and 16-bit mask
def parity(x: int) -> int:
    """
    Parity is 1 when number of set bits are odd,
        0 when number of set bits are even
    """
    # Here is the 3rd solution continued
    mask = 0xFFFF
    return LOOKUP[x >> 48] ^ LOOKUP[(x >> 32) & mask] ^ LOOKUP[(x >> 16) & mask] ^ LOOKUP[x & mask]

    # In addition to using an array-based cache, you can use multiple bit
    # processing to speed up performance (operating on multiple bits at a time
    # for the same binary number)
    #
    # An example would be:
    # 11010111 -> 1101 ^ 0111
    #             1010 -> 10 ^ 10
    #                     00 -> 0 ^ 0
    #                           0 & 0x1 (our bit mask) -> 0 (parity)
    #
    # this has a O(log(n)) runtime where n is the number of bits
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
    # return x & 1 <- also a valid return


    # This approach uses cache and bit mask to isolate an even 4 segments of
    # a binary number
    #
    # example     y1 y2 y3 y4                   cache   parity
    # 11010100 -> 11 01 01 00                   00      0
    #            0 ^ 1 ^ 1 ^ 0                  01      1
    #               1  ^  1                     10      1
    #                  0                        11      0
    #
    # Need to shift y1  y >> 3 * mask_size
    #               y2 (y >> 2 * mask_size) & bit_mask
    #               y3 (y >> mask_size) & bit_mask
    #               y4  y & bit_mask
    #
    # y2-y4 will have left over bits on the left of the cache alignment
    # AND with a bit_mask 00000011 to return the result of the
    # last two significant bits
    #
    # For large numbers assume a precomputed parity cache PC_PAR
    #
    #
    # mask_size = 16
    # bit_mask = 0xFFFF
    # return PC_PAR[x >> (3 * mask_size)] ^
    #        PC_PAR[(x >> (2 * mask_size)) & bit_mask] ^
    #        PC_PAR[(x >> mask_size) & bit_mask] ^
    #        PC_PAR[x & bit_mask]

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
