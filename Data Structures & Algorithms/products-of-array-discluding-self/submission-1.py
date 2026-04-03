import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1,0

        for i in range(len(nums)):
            if(nums[i] != 0):
                prod *= nums[i]
            else:
                zeros += 1
        if zeros > 1: return [0] * len(nums)

        final = [0] * len(nums)
        for i, c in enumerate(nums):
            if (zeros) != 0:
                final[i] = 0 if c else prod
            else:
                final[i] = (prod // nums[i])
        return final
        