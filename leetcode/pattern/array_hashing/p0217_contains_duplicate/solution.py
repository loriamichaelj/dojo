"""
# 217. Contains Duplicate
# URL: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting
# Pattern: Array & Hashing

Description:
    Given an integer array nums, return true if any value appears at least twice,
    and false if every element is distinct.

Examples:
    nums=[1,2,3,1]        →  True   (1 appears twice)
    nums=[1,2,3,4]        →  False  (all distinct)
    nums=[1,1,1,3,3,4,3,2,4,2]  →  True

Constraints:
    1 ≤ len(nums) ≤ 10^5
    -10^9 ≤ nums[i] ≤ 10^9

Approach:
    Single-pass hash set. For each element, check whether it has already been seen.
    If yes, return True immediately. Otherwise add it to the set and continue.

Complexity:
    Time:  O(n)  — one pass
    Space: O(n)  — set stores up to n elements
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
