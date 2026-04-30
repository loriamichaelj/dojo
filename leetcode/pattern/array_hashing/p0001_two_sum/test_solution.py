import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestTwoSum:
    def test_example_1(self, sol):
        assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_example_2(self, sol):
        assert sol.twoSum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_values(self, sol):
        assert sol.twoSum([3, 3], 6) == [0, 1]

    def test_negative_numbers(self, sol):
        assert sol.twoSum([-1, -2, -3, -4], -3) == [0, 1]

    def test_large_values(self, sol):
        assert sol.twoSum([1_000_000_000, -1_000_000_000], 0) == [0, 1]

    def test_answer_not_at_start(self, sol):
        assert sol.twoSum([1, 5, 3, 2], 5) == [2, 3]
