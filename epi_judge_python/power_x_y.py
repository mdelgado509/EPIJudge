from test_framework import generic_test


def power(x: float, y: int) -> float:
    # this next approach we use recursion and divide and conquer strategy
    # this time complexity run time is O(log(n))
    #
    if y == 0: return 1 # power of 0 result is 1
    if y == 1: return x # power of 1 result is x
    # define temp result by recursively calling power with y/2
    temp = power(x, int(y / 2))

    if y % 2 == 0: # if y is even
        return temp * temp
    else: # if y is odd
        if y > 0: return x * temp * temp
        else: return (temp * temp) / x # if y is odd and negative


    # a brute force approach is to multiply x y times
    # this achieves linear time complextiy and we can do better
    # by exploiting the properties of exponentiation
    #
    # if y is even then x^y is just (x^(y/2))^2
    # if y is odd then we just do x * (x^(y/2))^2
    #
    # We can examine each bit of y
    # if the LSB is 1 then we multiply the result by x
    # if it's even or odd x = x * x = x^2 etc... and y is right shifted 1 bit
    #
    # if y is odd we just set power = -power and x = 1/x
    #
    # this algo achieves O(n) time complexity where n is at most the index
    # of the MSB of y
    # result, power = 1.0, y
    # if y < 0: # if y is negative
    #     power, x = -power, 1.0 / x
    # while power: # examine each bit of power
    #     if power & 1:
    #         result = result * x
    #     x, power = x * x, power >> 1
    # return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
