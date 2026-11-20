class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        if len(nums) <= 3:
            return max(nums)
        dp1[0] = nums[0]
        dp2[1] = nums[1]

        for i in range(1,len(nums)-1):
            dp1[i] = max((dp1[i-2] if i >= 2 else 0)+nums[i], dp1[i-1])
        for i in range(2,len(nums)):    
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        return max(dp1[len(nums)-2],dp2[len(nums)-1])            
        