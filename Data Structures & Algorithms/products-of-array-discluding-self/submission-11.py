class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_0 = 1
        zeros = 0
        for i in range(len(nums)):
            total *= nums[i]
            if nums[i] != 0:
                total_0 *= nums[i]
            else:
                zeros += 1
        ret = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ret.append(total // nums[i])
            elif zeros == 1:
                ret.append(total_0)
            else:
                ret.append(0)
        return ret