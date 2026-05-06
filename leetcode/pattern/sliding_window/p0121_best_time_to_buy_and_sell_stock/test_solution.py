import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestMaxProfit:
    def test_example_1(self, sol):
        assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_example_2(self, sol):
        assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_single_price(self, sol):
        assert sol.maxProfit([5]) == 0

    def test_two_prices_profit(self, sol):
        assert sol.maxProfit([1, 2]) == 1

    def test_two_prices_no_profit(self, sol):
        assert sol.maxProfit([2, 1]) == 0

    def test_buy_at_start_sell_at_end(self, sol):
        assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

    def test_peak_at_start(self, sol):
        assert sol.maxProfit([9, 1, 2]) == 1

    def test_all_same(self, sol):
        assert sol.maxProfit([3, 3, 3, 3]) == 0

    def test_max_at_first_min_at_last(self, sol):
        assert sol.maxProfit([10, 5, 3, 1]) == 0

    def test_large_profit(self, sol):
        assert sol.maxProfit([0, 10000]) == 10000

    def test_profit_not_from_global_min_max(self, sol):
        # global min=1 at idx 1, global max=8 at idx 4, but best buy=2 sell=8
        assert sol.maxProfit([3, 1, 4, 1, 8, 2, 6]) == 7
