import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = nums[0]
        for i in range(1,len(nums)):
            total *= nums[i]
        final = []
        for i in range(len(nums)):
            if (nums[i]) != 0:
                final.append(total//nums[i])
            else:
                final.append(math.prod(nums[0:i]) * math.prod(nums[i+1:]))
        return final
        