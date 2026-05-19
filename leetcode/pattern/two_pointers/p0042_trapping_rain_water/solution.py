"""
# 42. Trapping Rain Water
# URL: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
# Topics: Array, Two Pointers, Stack, Dynamic Programming, Monotonic Stack
# Pattern: Two Pointers

Description:
    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.

Examples:
    height=[0,1,0,2,1,0,1,3,2,1,2,1]  →  6
    height=[4,2,0,3,2,5]               →  9

Constraints:
    n == height.length
    1 ≤ n ≤ 2 * 10^4
    0 ≤ height[i] ≤ 10^5

Approach:
    Two-pointer sweep inward from both ends. Maintain the running max seen from
    the left (max_left) and from the right (max_right). At each step, process
    the side with the smaller max: the water above that bar is guaranteed to be
    bounded by that smaller max regardless of what lies between the pointers,
    so we can safely accumulate max - height[pointer] and advance that pointer.

Complexity:
    Time:  O(n) — single pass
    Space: O(1) — two pointers, two max trackers
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water
