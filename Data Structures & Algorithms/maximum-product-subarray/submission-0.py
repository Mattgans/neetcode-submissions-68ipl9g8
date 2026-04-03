class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = nums[0]
        curmin, curmax = 1,1
        for num in nums:
            temp = curmax * num
            curmax = max(num * curmax, num * curmin, num)
            curmin = min(temp, num * curmin, num)
            ret = max(ret,curmax)
        return ret
