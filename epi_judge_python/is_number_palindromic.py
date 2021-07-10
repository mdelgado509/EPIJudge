"""
Write a program that takes an integer and determines if that integer's
representation as a decimal string is a palindrome

Note that if the input is negative, then its representation as a decimal
string cannot be palindromic, since it begins with -
"""
import math # first import math for approach 2

from test_framework import generic_test

def is_palindrome_number(x: int) -> bool:
    """
    Approach 3 - Use reverse digits approach and return result == x
    - Time Complexity - O(n) n is number of digits
    - Space Complexity - O(n)

    Approach 2 - Directly extract digits from input compare remove and repeat
    until mismatch is found else return True
    - Time Complexity - O(n/2) - n is number of digits
    - Space Complexity - O(1)

    Approach 1 - Brute-force convert the input to a string and then iterate
    through the string, pairwise comparing digits starting from the least
    significant digit (lsd) and the most significant digit (msd) working
    inwards stopping if there is a mismatch
    - Time Complexity - O(n/2) - n is number of digits
    - Space Complexity - O(n) - n is number of digits
        because of string representation
    """
    # Appraoch 3
    #
    # initialize result and |x|
    result, abs_x = 0, abs(x)
    # iterate over abs_x until its value is 0
    while abs_x:
        # add abs_x modulo 10 to result * 10
        result = abs_x % 10 + result * 10
        # integer divide abs_x by 10
        abs_x //= 10
    return False if x < 0 else result == x

    # Approach 2
    #
    # checks if x is 0 or less than 0
    if x <= 0:
        return x == 0
    # num_digits ~ log10(x) + 1
    # n = 5 if x = 31213
    # n = 4 if x = 3121
    # etc...
    num_digits = math.floor(math.log10(x)) + 1
    # create a msd_mask = 10 ** (num_digits)
    # msd = x // msd_mask
    # lsd = x % 10
    msd_mask = 10 ** (num_digits - 1)
    # iterate n // 2 times where n is the number of digits
    # for i in range(num_digits // 2):
    #
    # iterate until msd_mask is 1 (modified to eliminate unused i var)
    while msd_mask > 1:
        if x // msd_mask != x % 10:
            return False
        # msd lsd removal and msd mask shrinkage:
        x %= msd_mask # removes msd
        x //= 10 # removes lsd
        msd_mask //= 100 # shinks mask to size of new x
    return True

    # Approach 1
    #
    # checks if x is 0 or less than 0
    if x <= 0:
        return x == 0
    # str conversion uses O(n) space complexity where n is number of digits
    input_string = str(x)
    # defines index positions of lsd and msd
    lsd_index = 0
    msd_index = len(input_string) - 1 # bc 0 based index e.g. len(21) - 1 is index of msd
    # until the lsd_index is equal to or greater than msd_index
    while lsd_index < msd_index:
        if input_string[lsd_index] != input_string[msd_index]:
            return False
        lsd_index, msd_index = lsd_index + 1, msd_index - 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
