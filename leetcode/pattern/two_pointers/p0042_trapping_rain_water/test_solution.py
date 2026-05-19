import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_standard(solution):
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_example_valley(solution):
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9


# Edge cases
def test_single_bar(solution):
    assert solution.trap([5]) == 0


def test_two_bars(solution):
    assert solution.trap([3, 2]) == 0


def test_flat(solution):
    assert solution.trap([3, 3, 3]) == 0


def test_monotone_increasing(solution):
    assert solution.trap([1, 2, 3, 4, 5]) == 0


def test_monotone_decreasing(solution):
    assert solution.trap([5, 4, 3, 2, 1]) == 0


def test_v_shape(solution):
    assert solution.trap([3, 0, 3]) == 3


def test_all_zeros(solution):
    assert solution.trap([0, 0, 0, 0]) == 0


def test_single_pit(solution):
    # walls of height 2 around a zero — traps 2 units
    assert solution.trap([2, 0, 2]) == 2


def test_asymmetric_walls(solution):
    # right wall is taller; water level limited by left wall (height 1)
    assert solution.trap([1, 0, 3]) == 1
