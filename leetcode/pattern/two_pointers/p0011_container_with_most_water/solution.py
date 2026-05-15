"""
# 11. Container With Most Water
# URL: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Topics: Array, Two Pointers, Greedy
# Pattern: Two Pointers

Description:
    Given n non-negative integers height[0..n-1] where each represents a vertical
    line of that height at position i, find two lines that together with the x-axis
    form a container holding the most water. Return the maximum amount of water.

Examples:
    height=[1,8,6,2,5,4,8,3,7]  →  49
    height=[1,1]                 →  1

Constraints:
    n == height.length
    2 ≤ n ≤ 10^5
    0 ≤ height[i] ≤ 10^4

Approach:
    Start with the widest possible container (left=0, right=n-1). The area is
    min(height[left], height[right]) * (right - left). To potentially find a
    larger area we must increase the min height, so move the pointer at the
    shorter wall inward. Repeat until the pointers meet.

Complexity:
    Time:  O(n)  — each pointer moves at most n steps combined
    Space: O(1)  — pointers and a running max only
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return best
