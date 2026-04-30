import pytest

from .solution import LRUCache


@pytest.fixture
def cache2():
    return LRUCache(2)


class TestLRUCache:
    def test_leetcode_example(self, cache2):
        cache2.put(1, 1)
        cache2.put(2, 2)
        assert cache2.get(1) == 1
        cache2.put(3, 3)       # evicts key 2
        assert cache2.get(2) == -1
        cache2.put(4, 4)       # evicts key 1
        assert cache2.get(1) == -1
        assert cache2.get(3) == 3
        assert cache2.get(4) == 4

    def test_get_missing_key(self, cache2):
        assert cache2.get(99) == -1

    def test_update_existing_key(self, cache2):
        cache2.put(1, 10)
        cache2.put(1, 20)
        assert cache2.get(1) == 20

    def test_update_moves_to_front(self, cache2):
        cache2.put(1, 1)
        cache2.put(2, 2)
        cache2.put(1, 100)     # update key 1 → moves to MRU
        cache2.put(3, 3)       # evicts key 2 (LRU), not key 1
        assert cache2.get(1) == 100
        assert cache2.get(2) == -1
        assert cache2.get(3) == 3

    def test_get_refreshes_recency(self, cache2):
        cache2.put(1, 1)
        cache2.put(2, 2)
        cache2.get(1)          # 1 is now MRU; 2 becomes LRU
        cache2.put(3, 3)       # evicts key 2
        assert cache2.get(1) == 1
        assert cache2.get(2) == -1
        assert cache2.get(3) == 3

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        assert cache.get(1) == 1
        cache.put(2, 2)        # evicts key 1
        assert cache.get(1) == -1
        assert cache.get(2) == 2

    def test_fill_to_capacity_no_eviction(self, cache2):
        cache2.put(1, 1)
        cache2.put(2, 2)
        assert cache2.get(1) == 1
        assert cache2.get(2) == 2

    def test_overwrite_does_not_grow_cache(self, cache2):
        cache2.put(1, 1)
        cache2.put(2, 2)
        cache2.put(1, 99)      # overwrite, must not push count to 3
        cache2.put(3, 3)       # evicts LRU (key 2), not a third slot
        assert cache2.get(1) == 99
        assert cache2.get(2) == -1
        assert cache2.get(3) == 3
