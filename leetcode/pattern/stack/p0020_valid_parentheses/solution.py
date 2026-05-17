"""
# 20. Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Topics: String, Stack
# Pattern: Stack

Description:
    Given a string s containing only '(', ')', '{', '}', '[', ']', determine
    if the input string is valid. An input string is valid if:
      - Open brackets are closed by the same type of bracket.
      - Open brackets are closed in the correct order.
      - Every close bracket has a corresponding open bracket.

Examples:
    s="()"       →  True
    s="()[]{}"   →  True
    s="(]"       →  False
    s="([)]"     →  False
    s="{[]}"     →  True

Constraints:
    1 ≤ s.length ≤ 10^4
    s consists of parentheses only '()[]{}'

Approach:
    Use a stack. For each character: push open brackets onto the stack; for
    close brackets, check that the stack is non-empty and the top matches the
    expected opener. If any check fails, return False. After processing all
    characters, the string is valid only if the stack is empty.

Complexity:
    Time:  O(n)  — single pass through the string
    Space: O(n)  — stack holds at most n/2 open brackets
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        match = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
