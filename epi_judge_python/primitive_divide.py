from test_framework import generic_test


def divide(x: int, y: int) -> int:
    # compute quotient without arithmetical operators
    # use only addition subtraction and shifting operators
    #
    # book suggests to subtract 2^k * y from x where 2^k * y <= x
    # 2^k * y = y << k       and then add (1 << k) to the quotient
    # this gets more done with each round of subtraction
    #
    # This is O(n) time complexity where n is x/y in number of bits
    #
    # first define the result and the power k int
    # we set to 32 because we assume max bit size input is 64
    result, k = 0, 32
    # this is the 2ky variable
    y_pow_k = y << k
    while x >= y: # repeat until y > x
        while y_pow_k > x: # loop until x > y_pow_k
            y_pow_k >> 1 # right shift y_pow_k by 1
            k -= 1 # decrement k power
        result += 1 << k # add (1 << k) to the result
        x -= y_pow_k # subtract y_pow_k from x
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
