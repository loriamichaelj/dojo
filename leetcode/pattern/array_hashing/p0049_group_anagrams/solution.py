"""
# 49. Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Topics: Array, Hash Table, String, Sorting
# Pattern: Array & Hashing

Description:
    Given an array of strings strs, group the anagrams together and return
    the groups in any order.

Examples:
    strs=["eat","tea","tan","ate","nat","bat"]  →  [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs=[""]                                   →  [[""]]
    strs=["a"]                                  →  [["a"]]

Constraints:
    1 ≤ len(strs) ≤ 10^4
    0 ≤ len(strs[i]) ≤ 100
    strs[i] consists of lowercase English letters.

Approach:
    Sort each word's characters to produce a canonical key; all anagrams share
    the same key. Use a defaultdict to accumulate words under their key, then
    return the grouped values.

Complexity:
    Time:  O(n · k log k)  — n words, each sorted in O(k log k) where k = max word length
    Space: O(n · k)        — hash map stores all characters across all words

Notes:
    - Alternative key: a 26-element character-count tuple avoids sorting (O(k) per word),
      but in practice the sort approach is simpler and fast enough given k ≤ 100.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
