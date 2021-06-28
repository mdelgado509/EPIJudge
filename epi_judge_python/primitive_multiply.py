from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    # Next approach from book solution
    # for each set bit of x it adds 2^k * y to the result
    # k is the k-th bit that is set in x
    # time complexity O(n^2)
    def add(a, b):
        return a if b == 0 else add(a ^ b, (a & b) << 1)

    running_sum = 0
    while x:  # Examines each bit of x.
        # if last bit is 1
        if x & 1:
            # add y to running sum
            running_sum = add(running_sum, y)
        # right shift x to move to next bit and left shift y to increase
        # bit width by 1
        x, y = x >> 1, y << 1
    return running_sum
    #
    # brute force takes ~ 3 ms
    # O(2^n) time complexity where n is the number of bits in the input
    # still doesn't solve for how to multiply without add instructions
    result = 0
    while y:
        result = result + x
        y = y - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
