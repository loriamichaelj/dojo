"""
# 128. Longest Consecutive Sequence
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Topics: Array, Hash Table, Union Find
# Pattern: Array & Hashing

Description:
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence. Must run in O(n) time.

Examples:
    nums=[100,4,200,1,3,2]  →  4   (sequence: 1,2,3,4)
    nums=[0,3,7,2,5,8,4,6,0,1]  →  9   (sequence: 0–8)

Constraints:
    0 ≤ len(nums) ≤ 10^5
    -10^9 ≤ nums[i] ≤ 10^9

Approach:
    Build a hash set from nums. For each number that has no left neighbor
    (n-1 not in set), it is the start of a new sequence — count forward until
    the chain breaks. Track the maximum length seen.

    Only starting from sequence heads avoids counting the same sequence
    multiple times, keeping the overall work O(n).

Complexity:
    Time:  O(n)  — each number is visited at most twice
    Space: O(n)  — hash set
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                best = max(best, length)
        return best
