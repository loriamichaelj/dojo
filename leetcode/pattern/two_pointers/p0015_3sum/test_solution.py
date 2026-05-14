import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


def sorted_triplets(triplets):
    return sorted(tuple(sorted(t)) for t in triplets)


# LeetCode examples
def test_example_mixed(solution):
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted_triplets(result) == sorted_triplets([[-1, -1, 2], [-1, 0, 1]])


def test_example_no_solution(solution):
    assert solution.threeSum([0, 1, 1]) == []


def test_example_all_zeros(solution):
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]


# Edge cases
def test_all_positive_no_solution(solution):
    assert solution.threeSum([1, 2, 3]) == []


def test_all_negative_no_solution(solution):
    assert solution.threeSum([-3, -2, -1]) == []


def test_multiple_triplets(solution):
    result = solution.threeSum([-4, -1, -1, 0, 1, 2])
    assert sorted_triplets(result) == sorted_triplets([[-1, -1, 2], [-1, 0, 1]])


def test_duplicates_produce_one_triplet(solution):
    result = solution.threeSum([-2, 0, 0, 2, 2])
    assert sorted_triplets(result) == sorted_triplets([[-2, 0, 2]])


def test_minimum_length(solution):
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]


def test_large_range(solution):
    result = solution.threeSum([-100000, 0, 100000])
    assert result == [[-100000, 0, 100000]]
