"""
# 242. Valid Anagram
# URL: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# Pattern: Array & Hashing

Description:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An anagram uses all original letters exactly once.

Examples:
    s="anagram", t="nagaram"  →  True
    s="rat",     t="car"      →  False

Constraints:
    1 ≤ len(s), len(t) ≤ 5 * 10^4
    s and t consist of lowercase English letters.

Approach:
    Early-exit on length mismatch, then build a frequency map for s and decrement
    for each character in t. If any count goes negative, the strings are not anagrams.

Complexity:
    Time:  O(n)  — two passes over strings of length n
    Space: O(1)  — at most 26 keys in the frequency map
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq: dict[str, int] = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in t:
            freq[ch] = freq.get(ch, 0) - 1
            if freq[ch] < 0:
                return False
        return True
