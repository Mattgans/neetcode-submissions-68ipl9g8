class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minbuy = prices[0]
        for sell in prices:
            best = max(best, sell-minbuy)
            minbuy = min(minbuy,sell)
        return best
            
        