"""
# 560. Subarray Sum Equals K
# URL: https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium
# Topics: Array, Hash Table, Prefix Sum
# Pattern: Prefix Sum

Description:
    Given an array of integers nums and an integer k, return the total number
    of subarrays whose sum equals k.

Examples:
    nums=[1,1,1], k=2  →  2
    nums=[1,2,3], k=3  →  2   ([1,2] and [3])

Constraints:
    1 ≤ nums.length ≤ 2 * 10^4
    -1000 ≤ nums[i] ≤ 1000
    -10^7 ≤ k ≤ 10^7

Approach:
    Maintain a running prefix sum. At each index, the number of subarrays
    ending here that sum to k equals the number of times (prefix_sum - k)
    has appeared as a prefix sum before. Store prefix sum frequencies in a
    hash map, seeded with {0: 1} to handle subarrays that start at index 0.

Complexity:
    Time:  O(n)  — single pass
    Space: O(n)  — prefix sum frequency map
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq: dict[int, int] = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count
