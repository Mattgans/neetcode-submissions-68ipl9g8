class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top = prices[0]
        made = 0
        for i in prices:
            made = max(made, i-top)
            top = min(top, i)
        return made