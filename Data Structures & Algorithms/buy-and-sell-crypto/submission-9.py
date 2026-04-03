class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute Force
        # best = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         best = max(prices[j] - prices[i],best)
        # return best
        # two pointer
        left = 0
        right = 1
        best = 0
        while right < len(prices):
            cur = prices[right]-prices[left]
            if prices[right] > prices[left]:
                best = max(best,cur)
            else:
                left = right
            right += 1
        return best
        # greedy Kandane's Algo