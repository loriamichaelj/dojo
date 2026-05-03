"""
# 347. Top K Frequent Elements
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort
# Pattern: Heap / Priority Queue

Description:
    Given an integer array nums and an integer k, return the k most frequent
    elements. The answer may be returned in any order.

Examples:
    nums=[1,1,1,2,2,3], k=2  →  [1,2]
    nums=[1], k=1             →  [1]

Constraints:
    1 ≤ k ≤ len(nums) ≤ 10^5
    -10^4 ≤ nums[i] ≤ 10^4
    The answer is guaranteed to be unique.

Approach:
    Count frequencies with Counter, then use heapq.nlargest to extract the k
    elements with the highest counts. nlargest runs in O(n log k) time, which
    beats a full sort for small k.

    Alternative — bucket sort: create len(nums)+1 frequency buckets, scatter
    each element into its bucket, then scan right-to-left collecting until k
    elements are gathered. O(n) time and space, no heap needed.

Complexity:
    Time:  O(n log k)  — counting O(n), heap extraction O(n log k)
    Space: O(n)        — frequency map

Notes:
    - The bucket-sort approach achieves O(n) but is harder to read; the heap
      approach is idiomatic Python and clearly communicates intent.
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        return heapq.nlargest(k, counts, key=counts.__getitem__)
