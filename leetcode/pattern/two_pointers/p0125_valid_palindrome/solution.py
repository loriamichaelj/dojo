"""
# 125. Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Topics: Two Pointers, String
# Pattern: Two Pointers

Description:
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the same
    forward and backward. Given a string s, return true if it is a palindrome,
    or false otherwise.

Examples:
    "A man, a plan, a canal: Panama"  →  True
    "race a car"                       →  False
    " "                                →  True

Constraints:
    1 ≤ s.length ≤ 2 * 10^5
    s consists only of printable ASCII characters.

Approach:
    Use two pointers starting at each end of the string. Advance each pointer
    inward past non-alphanumeric characters, then compare the lowercased
    characters at both pointers. If any pair mismatches, return False.

Complexity:
    Time:  O(n)  — single pass, each character visited at most once
    Space: O(1)  — pointers only, no copy of the string
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
