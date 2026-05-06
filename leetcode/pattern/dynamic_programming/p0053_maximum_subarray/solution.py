"""
# 53. Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Topics: Array, Divide and Conquer, Dynamic Programming
# Pattern: Dynamic Programming (Kadane's Algorithm)

Description:
    Given an integer array nums, find the subarray with the largest sum and
    return its sum.

Examples:
    nums=[-2,1,-3,4,-1,2,1,-5,4]  →  6  (subarray [4,-1,2,1])
    nums=[1]                        →  1
    nums=[5,4,-1,7,8]              →  23 (whole array)

Constraints:
    1 ≤ nums.length ≤ 10^5
    -10^4 ≤ nums[i] ≤ 10^4

Approach:
    Kadane's algorithm: at each index decide whether to extend the current
    subarray or start a new one from this element. Extending is only worth it
    if the running sum is positive; otherwise, restart. Track the global max
    across all positions.

    current = max(num, current + num)
    max_sum = max(max_sum, current)

Complexity:
    Time:  O(n)  — single pass
    Space: O(1)  — two scalar variables
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = max_sum = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            max_sum = max(max_sum, current)
        return max_sum
