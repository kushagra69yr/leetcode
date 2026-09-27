class Solution:
    def maxProfit(self,prices):
        low,best = prices[0], 0
        for p in prices[1:]:
            if p < low :
                low = p
            elif p - low > best:
                best = p - low
        return best