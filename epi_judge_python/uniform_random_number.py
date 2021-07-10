"""
How would you implement a random number generator that generates a random
integer i between a and b, inclusive, given a random number generator that
produces zero or one with equal probability. All values in [a,b] should be
equal likely.
"""
import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    """
    Example: 1-6
    number_of_outcomes = 6
    can produce results:
    0b000 0b001 0b010 0b011 0b100 0b101 0b110 0b111

    if 0b110 or 0b111 is produced then result and i are reset and the
    loop runs until result < number_of_outcomes

    O(log(b - a + 1)) where b is the upper bound and a is the lower bound

    or... O(log(n)) where n is the number of outcomes.
    """
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
