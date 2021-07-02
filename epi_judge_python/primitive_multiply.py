from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    # Next approach from book solution
    #
    # first we need a function for addition
    # we are going to use & and << to simulate carrying in bin addition
    # for example 1 & 1 = 1 is a position where addition is going to result
    # in 10 but we need to carry the 1 over
    # so if b represents the carry b = 1 & 1 = 1 << 1 = 10
    #
    # we are going to use ^ to perform the actual addition
    # but in each iteration of addition we redefine a and b until the
    # carry var b = 0
    def add(a, b):
        return a if b == 0 else add(a ^ b, (a & b) << 1)
        # this is a breakdown of the above line of code
        #
        # # if the carry equals 0 return the sum a
        # if b == 0:
        #     return a
        # # else define the carry
        # b = (a & b) << 1
        # # perform the addition
        # a = a ^ b
        # # recursively call add function with new values
        # add(a, b)

    # define result variable
    result = 0
    while x: # examines each bit of y or returns 0 if y is 0
        if x & 1: # if the last bit is 1
            result = add(result, y) # add x to the result
        # left shift x to carry to next bit position
        # right shift y to expose the next bit
        x, y = x >> 1, y << 1
    return result

    #
    # brute force takes ~ 3 ms
    # O(2^n) time complexity where n is the number of bits in the input
    # still doesn't solve for how to multiply without add instructions
    # result = 0
    # while y:
    #     result = result + x
    #     y = y - 1
    # return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
