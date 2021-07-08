"""
Write a program that takes an integer and determines if that integer's
representation as a decimal string is a palindrome

Note that if the input is negative, then its representation as a decimal
string cannot be palindromic, since it begins with -
"""

from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    """
    Approach 2 -


    Approach 1 - Brute-force convert the input to a string and then iterate
    through the string, pairwise comparing digits starting from the least
    significant digit (lsd) and the most significant digit (msd) working
    inwards stopping if there is a mismatch

    Time Complexity - O(n) - n is number of digits
    Starting to think it's O(n/2) ???
    Space Complexity - O(n) - n is number of digits
    because of string representation
    """
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
