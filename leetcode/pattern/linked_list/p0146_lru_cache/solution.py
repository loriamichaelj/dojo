"""
# 146. LRU Cache
# URL: https://leetcode.com/problems/lru-cache/
# Difficulty: Medium
# Topics: Hash Table, Linked List, Design, Doubly-Linked List
# Pattern: Linked List

Description:
    Design a data structure that follows the Least Recently Used (LRU) cache
    eviction policy.

    Implement LRUCache:
        LRUCache(int capacity)  — initialize with positive capacity
        int get(int key)        — return value if key exists, else -1
        void put(int key, int value) — insert/update key; evict LRU entry if
                                       over capacity

    Both get and put must run in O(1) average time.

Examples:
    cache = LRUCache(2)
    cache.put(1, 1)   # cache: {1:1}
    cache.put(2, 2)   # cache: {1:1, 2:2}
    cache.get(1)      # → 1,  cache: {2:2, 1:1}  (1 is now most recent)
    cache.put(3, 3)   # evicts key 2; cache: {1:1, 3:3}
    cache.get(2)      # → -1 (evicted)
    cache.put(4, 4)   # evicts key 1; cache: {3:3, 4:4}
    cache.get(1)      # → -1 (evicted)
    cache.get(3)      # → 3
    cache.get(4)      # → 4

Constraints:
    1 ≤ capacity ≤ 3000
    0 ≤ key ≤ 10^4
    0 ≤ value ≤ 10^5
    At most 2 * 10^5 calls to get and put combined.

Approach:
    Maintain a doubly-linked list ordered from most- to least-recently used,
    plus a hash map from key to node. Two sentinel nodes (head = MRU side,
    tail = LRU side) eliminate all edge-case boundary checks.

    get: look up node in map, splice it to the front, return its value.
    put: if key exists remove the old node; create a new node and insert at
         front; if len(cache) > capacity evict the node just before tail.

Complexity:
    Time:  O(1) amortized for both get and put
    Space: O(capacity) — at most capacity nodes in the list and map
"""


class _Node:
    __slots__ = ("key", "val", "prev", "next")

    key: int
    val: int
    prev: "_Node | None"
    next: "_Node | None"

    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, _Node] = {}
        self._head = _Node()  # MRU sentinel
        self._tail = _Node()  # LRU sentinel
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next  # type: ignore[union-attr]
        node.next.prev = node.prev  # type: ignore[union-attr]

    def _insert_front(self, node: _Node) -> None:
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node  # type: ignore[union-attr]
        self._head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = _Node(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.capacity:
            lru = self._tail.prev
            self._remove(lru)  # type: ignore[arg-type]
            del self.cache[lru.key]  # type: ignore[union-attr]
