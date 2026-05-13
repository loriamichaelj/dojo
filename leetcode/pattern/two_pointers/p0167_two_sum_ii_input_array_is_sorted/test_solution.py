import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_basic(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_example_middle(solution):
    assert solution.twoSum([2, 3, 4], 6) == [1, 3]


def test_example_negatives(solution):
    assert solution.twoSum([-1, 0], -1) == [1, 2]


# Edge cases
def test_two_element_array(solution):
    assert solution.twoSum([1, 2], 3) == [1, 2]


def test_target_uses_last_two(solution):
    assert solution.twoSum([1, 3, 5, 7], 12) == [3, 4]


def test_target_uses_first_and_last(solution):
    assert solution.twoSum([1, 4, 6, 8], 9) == [1, 4]


def test_duplicates_in_array(solution):
    assert solution.twoSum([1, 1, 3, 5], 2) == [1, 2]


def test_negative_target(solution):
    assert solution.twoSum([-4, -3, -1, 0], -7) == [1, 2]


def test_zero_in_sum(solution):
    assert solution.twoSum([-3, 0, 3, 5], 0) == [1, 3]
