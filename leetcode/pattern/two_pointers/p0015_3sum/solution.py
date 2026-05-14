"""
# 15. 3Sum
# URL: https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Topics: Array, Two Pointers, Sorting
# Pattern: Two Pointers

Description:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
    The solution set must not contain duplicate triplets.

Examples:
    nums=[-1, 0, 1, 2, -1, -4]  →  [[-1, -1, 2], [-1, 0, 1]]
    nums=[0, 1, 1]               →  []
    nums=[0, 0, 0]               →  [[0, 0, 0]]

Constraints:
    3 ≤ nums.length ≤ 3000
    -10^5 ≤ nums[i] ≤ 10^5

Approach:
    Sort the array so duplicates are adjacent and the two-pointer technique applies.
    Fix each element nums[i] as the first element of the triplet, then run a
    two-pointer sweep over the remaining suffix to find pairs that sum to
    -nums[i]. Skip duplicate values of nums[i] (and of the two inner pointers
    after a hit) to avoid emitting identical triplets.

Complexity:
    Time:  O(n^2) — O(n log n) sort + O(n) two-pointer sweep for each of n pivots
    Space: O(1)   — output aside; sort is in-place
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
