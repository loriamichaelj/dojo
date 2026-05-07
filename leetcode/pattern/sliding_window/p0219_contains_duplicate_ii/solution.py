"""
# 219. Contains Duplicate II
# URL: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Topics: Array, Hash Table, Sliding Window
# Pattern: Sliding Window (fixed-size hash set)

Description:
    Given an integer array nums and an integer k, return true if there exist two
    distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.

Examples:
    nums=[1,2,3,1], k=3  →  True   (i=0, j=3, diff=3)
    nums=[1,0,1,1], k=1  →  True   (i=2, j=3, diff=1)
    nums=[1,2,3,1,2,3], k=2  →  False

Constraints:
    1 ≤ nums.length ≤ 10^5
    -10^9 ≤ nums[i] ≤ 10^9
    0 ≤ k ≤ 10^5

Approach:
    Maintain a sliding window of the last k elements in a hash set. For each
    new element, check if it already exists in the window (duplicate within
    distance k). Then add the element and evict the element that fell out of
    the window (nums[i - k]) to keep the window exactly size k.

Complexity:
    Time:  O(n)  — single pass, O(1) set operations
    Space: O(k)  — window set holds at most k+1 elements
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window: set[int] = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
