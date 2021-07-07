"""
Write a program which takes an integer and returns the integer corresponding to
the digits of the input written in reverse order. For example, the reverse of
42 is 24, and the reverse of -314 is -413.

Hint: How would you solve the same problem if the input is a string
"""

from test_framework import generic_test


def reverse(x: int) -> int:
    """
    Approach 3 - Avoid string conversion and leverage modulo operation and
    integer division.
    Time Complexity - O(n) where n is the number of digits

    Approach 2 - Use slicing to reverse the converted string
    Time Complexity - Slightly faster ??? Worst case of slicing O(n)

    Approach 1 - Convert to string, traverse each character from the end, add
    each character to the new string, and convert the result to an integer.
    Time Complexity - O(n) where n is number of digits
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
    return -result if x < 0 else result

    # Approach 2
    #
    # convert |int| to string
    abs_int_string = str(abs(x))
    # reverse string with slicing
    reverse_string = abs_int_string[::-1]
    # convert string to int
    result = int(reverse_string)
    return -result if x < 0 else result

    # Approach 1
    #
    # initialize string to hold reversed characters
    new_string = ''
    # convert |int| to string
    abs_int_string = str(abs(x))
    # define last index position
    index = len(abs_int_string)
    # iterate over abs_int_string and add characters to new_string
    while index:
        index -= 1
        new_string += abs_int_string[index]
    # convert new_string to int
    result = int(new_string)
    return -result if x < 0 else result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
