import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_multiple_trades(solution):
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_example_monotone_increase(solution):
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4


def test_example_monotone_decrease(solution):
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0


# Edge cases
def test_single_day(solution):
    assert solution.maxProfit([5]) == 0


def test_two_days_profit(solution):
    assert solution.maxProfit([1, 10]) == 9


def test_two_days_no_profit(solution):
    assert solution.maxProfit([10, 1]) == 0


def test_flat_prices(solution):
    assert solution.maxProfit([3, 3, 3, 3]) == 0


def test_valley_peak_valley(solution):
    # Buy at 1, sell at 5, buy at 2, sell at 6 → profit 8
    assert solution.maxProfit([3, 1, 5, 2, 6]) == 8
