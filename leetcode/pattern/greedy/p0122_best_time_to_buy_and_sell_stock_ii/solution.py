"""
# 122. Best Time to Buy and Sell Stock II
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Greedy
# Pattern: Greedy

Description:
    You are given an integer array prices where prices[i] is the price of a
    given stock on the i-th day. On each day you may decide to buy and/or sell
    the stock. You can hold at most one share at a time, but you may buy and
    immediately sell on the same day. Return the maximum profit you can achieve.

Examples:
    prices=[7,1,5,3,6,4]  →  7   (buy day 1, sell day 2; buy day 3, sell day 4)
    prices=[1,2,3,4,5]    →  4   (buy day 0, sell day 4)
    prices=[7,6,4,3,1]    →  0   (no profitable transaction)

Constraints:
    1 ≤ prices.length ≤ 3 * 10^4
    0 ≤ prices[i] ≤ 10^4

Approach:
    Greedy: every upward move in price is capturable. Sum all positive
    day-over-day differences. This is equivalent to riding every profitable
    sub-interval, which together compose the globally optimal trade sequence.

    profit += max(0, prices[i] - prices[i-1])  for i in 1..n-1

Complexity:
    Time:  O(n)  — single pass
    Space: O(1)  — one scalar accumulator
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
