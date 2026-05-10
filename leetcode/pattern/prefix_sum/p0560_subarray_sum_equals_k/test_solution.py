import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_repeated_ones(solution):
    assert solution.subarraySum([1, 1, 1], 2) == 2


def test_example_mixed(solution):
    assert solution.subarraySum([1, 2, 3], 3) == 2


# Edge cases
def test_single_element_equals_k(solution):
    assert solution.subarraySum([5], 5) == 1


def test_single_element_not_k(solution):
    assert solution.subarraySum([1], 5) == 0


def test_negative_numbers(solution):
    # [1, -1] sums to 0, [1, -1, 1, -1] sums to 0, [-1, 1] sums to 0
    assert solution.subarraySum([1, -1, 1, -1], 0) == 4


def test_k_zero_all_zeros(solution):
    assert solution.subarraySum([0, 0, 0], 0) == 6


def test_no_valid_subarray(solution):
    assert solution.subarraySum([1, 2, 3], 7) == 0


def test_entire_array_is_subarray(solution):
    assert solution.subarraySum([1, 2, 3], 6) == 1


def test_negative_k(solution):
    assert solution.subarraySum([-1, -2, -3], -3) == 2
