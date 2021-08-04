from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # Book solution: O(n^2) solution 
    # set sign to 1 if first elements have different signs
    sign = -1 if (num1[0] < 0) != (num2[0] < 0) else 1
    # set first elements to their absolute value
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # set result array to list of 0's of length len(num1) + len(num2)
    # this is the maximum length we would need for extra product digits
    result = [0] * (len(num1) + len(num2))
    # for each digit in num1 (back to front)
    # multiply by each digit of j (back to front)
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            # multiply each digit position
            result[i + j + 1] += num1[i] * num2[j]
            # carry the one to the next element
            # by reassigning the result and int division by 10
            result[i + j] += result[i + j + 1] // 10
            # extract remainder of result / 10
            result[i + j + 1] %= 10

    # remove leading zeros
    result = result[next((i for i, x in enumerate(result)
                         if x != 0), len(result)):] or [0]
    # multiply first element by sign
    result[0] *= sign
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
