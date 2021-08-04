from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # This is modeled after the grade-school addition algorithm
    # O(n) time complexity and O(1) space (slightly altered from book)

    # Start from least significant digit (in our case the back
    # of the list) and add 1
    A[-1] += 1

    # Then iterate from last to the second digit (don't include the first)
    for i in reversed(range(1, len(A))):
        # If A[i] is 10 then set to 0 and increment A[i - 1]
        if A[i] == 10:
            A[i] = 0
            A[i - 1] += 1

    # if the A[0] digit is 10 set to 1 and append a 0
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
