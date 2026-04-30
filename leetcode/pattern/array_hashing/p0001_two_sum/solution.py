"""
# 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topics: Array, Hash Table
# Pattern: Array & Hashing

Description:
    Given an array of integers nums and an integer target, return the indices of the
    two numbers that add up to target. Each input has exactly one solution, and you
    may not use the same element twice.

Examples:
    nums=[2,7,11,15], target=9  →  [0, 1]   (2+7=9)
    nums=[3,2,4],     target=6  →  [1, 2]   (2+4=6)
    nums=[3,3],       target=6  →  [0, 1]   (3+3=6)

Constraints:
    2 ≤ len(nums) ≤ 10^4
    -10^9 ≤ nums[i] ≤ 10^9
    -10^9 ≤ target ≤ 10^9
    Exactly one valid answer exists.

Approach:
    Single-pass hash map. For each element, check whether its complement
    (target - num) was already seen. If yes, return the two indices immediately.
    Otherwise record num → index and continue.

Complexity:
    Time:  O(n)  — one pass
    Space: O(n)  — hash map stores up to n entries

Notes:
    - Brute force is O(n²) — too slow for n=10^4.
    - Insertion order doesn't matter; complement check handles it.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
