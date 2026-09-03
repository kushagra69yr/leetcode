class Solution:
    def maxProfit(self, prices):
        buy, profit = prices[0], 0

        for i in prices:
            buy = min(buy, i)
            profit = max(profit, i - buy)

        return profit