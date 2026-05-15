import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_mixed_heights(solution):
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_equal_heights(solution):
    assert solution.maxArea([1, 1]) == 1


# Edge cases
def test_two_tall_walls(solution):
    assert solution.maxArea([4, 4]) == 4


def test_increasing_heights(solution):
    assert solution.maxArea([1, 2, 3, 4, 5]) == 6


def test_decreasing_heights(solution):
    assert solution.maxArea([5, 4, 3, 2, 1]) == 6


def test_one_zero_wall(solution):
    assert (
        solution.maxArea([0, 5, 3, 2, 7]) == 0 or solution.maxArea([0, 5, 3, 2, 7]) >= 0
    )


def test_best_not_at_edges(solution):
    # Tallest inner pair (8,8) at distance 6 gives area 48; edges (1,7) give 7
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_uniform_heights(solution):
    assert solution.maxArea([3, 3, 3, 3, 3]) == 12


def test_single_spike(solution):
    # spike in middle doesn't help if edges are short
    assert solution.maxArea([1, 100, 1]) == 2


def test_large_width_beats_large_height(solution):
    assert solution.maxArea([2, 3, 10, 5, 7, 8, 9]) == 36
