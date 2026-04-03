class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        ret = 0
        while(r < len(prices)):
            if prices[r] > prices[l]:
                ret = max(prices[r]-prices[l],ret)
            else:
                l = r
            r += 1
        return ret




        # # brute force
        # m = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         m = max(m,prices[j]-prices[i])
        # return m

        