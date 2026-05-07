import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_true_distance_equals_k(solution):
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) is True


def test_example_true_adjacent(solution):
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) is True


def test_example_false(solution):
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False


# Edge cases
def test_single_element(solution):
    assert solution.containsNearbyDuplicate([1], 1) is False


def test_k_zero(solution):
    # k=0 means i==j, impossible for distinct indices
    assert solution.containsNearbyDuplicate([1, 1], 0) is False


def test_all_same_large_k(solution):
    assert solution.containsNearbyDuplicate([5, 5, 5, 5], 100) is True


def test_duplicate_just_outside_window(solution):
    # duplicate exists but distance is k+1
    assert solution.containsNearbyDuplicate([1, 2, 3, 4, 1], 3) is False


def test_duplicate_at_window_boundary(solution):
    # distance exactly k — should return True
    assert solution.containsNearbyDuplicate([1, 2, 3, 4, 1], 4) is True
