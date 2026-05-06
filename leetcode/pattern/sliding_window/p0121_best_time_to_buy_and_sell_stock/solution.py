"""
# 121. Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Topics: Array, Dynamic Programming
# Pattern: Sliding Window

Description:
    You are given an array prices where prices[i] is the price of a given
    stock on the ith day. You want to maximize your profit by choosing a
    single day to buy one stock and choosing a different day in the future
    to sell that stock. Return the maximum profit you can achieve. If you
    cannot achieve any profit, return 0.

Examples:
    prices=[7,1,5,3,6,4]  →  5  (buy day 1 at 1, sell day 4 at 6)
    prices=[7,6,4,3,1]    →  0  (prices only decline)

Constraints:
    1 ≤ prices.length ≤ 10^5
    0 ≤ prices[i] ≤ 10^4

Approach:
    Single pass with two implicit pointers: track the minimum price seen so
    far (left/buy candidate) and the current price (right/sell candidate).
    At each step, compute the candidate profit and update the running maximum.
    When the current price drops below the tracked minimum, advance the buy
    pointer — there is no reason to sell at a loss when a cheaper buy exists.

Complexity:
    Time:  O(n)  — single pass
    Space: O(1)  — two scalar variables
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
