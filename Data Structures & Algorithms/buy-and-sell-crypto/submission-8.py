class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute Force
        best = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                best = max(prices[j] - prices[i],best)
        return best
        # two pointer
        # greedy Kandane's Algo