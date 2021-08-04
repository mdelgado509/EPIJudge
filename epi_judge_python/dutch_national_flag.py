import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # In this approach we use 4 subarrays
    # 1. element is less than pivot    : A[equal]  < pivot : A[:smaller]
    # 2. element is equal to pivot     : A[equal] == pivot : A[smaller:equal]
    # 3. element is unclassified       : A[equal]  ? pivot : A[equal:larger]
    # 4. element is greater than pivot : A[equal]  > pivot : A[larger:]
    # O(n) time O(1) space
    # Approach 4:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger: # while there are unclassified elements
        # A[equal] are the unclassified elements
        if A[equal] < pivot:
            # switch upperbound of smaller subarray with current
            # unclassified element
            # increment both pointers by 1
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            # increase the unclassified pointer to 1
            # increases unclassified subarray by 1
            equal += 1
        else: # A[equal] > pivot
            # decrement larger subarray upperbound pointer by 1
            # switch lower bound of larger subarray with
            # current unclassified element
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


    # In this approach we use two pointers to keep track
    # of the next available position to place elements
    # smaller than the pivot in the front. and elements
    # larger than the pivot in the back of the array
    # this has O(n) and O(1) time and space complexity, respectively
    # Approach 3:
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    # at the front of the array
    front_pointer = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[front_pointer] = A[front_pointer], A[i]
            front_pointer += 1
    # Second pass: group elements larger than pivot
    # at the back of the array
    back_pointer = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[back_pointer] = A[back_pointer], A[i]
            back_pointer -= 1


    # this first approach improves a O(n) space complexity
    # to O(1) by using the array itself to sort, but the
    # time complexity is O(n^2) two nested loops
    # Approach 2:
    pivot = A[pivot_index]
    # First pass: start from front and move elements smaller than
    # pivot to the front of the array
    for i in range(len(A)):
        # Look for element smaller than pivot to place at index i
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break # switch elements and move i to the next index
    # Second pass: from the back group elements larger than pivot at
    # the back of the array
    for i in reversed(range(len(A))):
        # Look for a larger element. Stop when we reach an element larger
        # Than pivot and switch with element at i (from te back)
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Approach 2: Create three subarrays
    # O(n) time O(n) space
    pivot = A[pivot_index]
    smaller = []
    equal = []
    larger = []

    for val in A:
        if val < pivot:
            smaller.append(val)
        elif val == pivot:
            equal.append(val)
        else: # val >
            larger.append(val)
    for i in range(len(A)):
        if smaller:
            A[i] = smaller.pop()
        elif equal:
            A[i] = equal.pop()
        else:
            A[i] = larger.pop()

    # Approach 1: Built in sort method
    # O(nlog(n))
    A.sort()

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
