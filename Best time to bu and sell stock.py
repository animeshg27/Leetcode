"""
Question: You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0 , 1
        maxpr = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxpr = max(maxpr, profit)
            else:
                l = r
            r += 1
        return maxpr 

    
