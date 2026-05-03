import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestTopKFrequent:
    def test_example_1(self, sol):
        assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    def test_example_2(self, sol):
        assert sol.topKFrequent([1], 1) == [1]

    def test_k_equals_n_distinct(self, sol):
        assert sorted(sol.topKFrequent([1, 2, 3], 3)) == [1, 2, 3]

    def test_all_same(self, sol):
        assert sol.topKFrequent([5, 5, 5, 5], 1) == [5]

    def test_negatives(self, sol):
        assert sorted(sol.topKFrequent([-1, -1, 2, 2, 2], 1)) == [2]

    def test_tie_broken_by_k(self, sol):
        result = sol.topKFrequent([1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2]

    def test_large_k(self, sol):
        nums = [1] * 5 + [2] * 4 + [3] * 3 + [4] * 2 + [5] * 1
        assert sorted(sol.topKFrequent(nums, 3)) == [1, 2, 3]
