import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestContainsDuplicate:
    def test_example_1(self, sol):
        assert sol.containsDuplicate([1, 2, 3, 1]) is True

    def test_example_2(self, sol):
        assert sol.containsDuplicate([1, 2, 3, 4]) is False

    def test_example_3(self, sol):
        assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    def test_single_element(self, sol):
        assert sol.containsDuplicate([1]) is False

    def test_two_identical(self, sol):
        assert sol.containsDuplicate([7, 7]) is True

    def test_negative_numbers(self, sol):
        assert sol.containsDuplicate([-1, -2, -3, -1]) is True

    def test_all_distinct_negative(self, sol):
        assert sol.containsDuplicate([-1, -2, -3, -4]) is False

    def test_duplicate_at_end(self, sol):
        assert sol.containsDuplicate([1, 2, 3, 4, 5, 1]) is True
