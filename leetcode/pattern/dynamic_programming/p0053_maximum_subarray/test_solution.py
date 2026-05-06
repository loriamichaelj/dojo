import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_mixed(solution):
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example_single(solution):
    assert solution.maxSubArray([1]) == 1


def test_example_all_positive(solution):
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23


# Edge cases
def test_all_negative(solution):
    assert solution.maxSubArray([-3, -1, -2]) == -1


def test_single_negative(solution):
    assert solution.maxSubArray([-7]) == -7


def test_large_negative_bookends(solution):
    # Optimal subarray is in the middle
    assert solution.maxSubArray([-10, 2, 3, -10]) == 5


def test_alternating(solution):
    assert solution.maxSubArray([1, -1, 1, -1, 1]) == 1
