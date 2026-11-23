class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minl = prices[0]
        for price in prices:
            best = max(best, price-minl)
            minl = min(minl,price)
        return best
        