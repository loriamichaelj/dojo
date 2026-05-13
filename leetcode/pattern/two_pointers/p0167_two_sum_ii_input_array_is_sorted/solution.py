"""
# 167. Two Sum II - Input Array Is Sorted
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Topics: Array, Two Pointers, Binary Search
# Pattern: Two Pointers

Description:
    Given a 1-indexed array of integers numbers that is already sorted in
    non-decreasing order, find two numbers such that they add up to a specific
    target number. Return the indices of the two numbers as [index1, index2]
    where 1 <= index1 < index2 <= numbers.length. Each input has exactly one
    solution and you may not use the same element twice.

Examples:
    numbers=[2,7,11,15], target=9   →  [1, 2]
    numbers=[2,3,4],     target=6   →  [1, 3]
    numbers=[-1,0],      target=-1  →  [1, 2]

Constraints:
    2 ≤ numbers.length ≤ 3 * 10^4
    -1000 ≤ numbers[i] ≤ 1000
    numbers is sorted in non-decreasing order.
    -1000 ≤ target ≤ 1000
    Exactly one solution exists.

Approach:
    Place one pointer at the start and one at the end. If the sum equals the
    target, return the 1-indexed positions. If the sum is too small, advance
    the left pointer to increase it; if too large, retreat the right pointer.
    The sorted order guarantees convergence to the unique solution.

Complexity:
    Time:  O(n)  — single pass, pointers move at most n steps combined
    Space: O(1)  — pointers only
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
