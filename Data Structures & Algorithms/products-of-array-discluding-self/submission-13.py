class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = False
        allz = False
        for i in nums:
            if i != 0:
                total *= i
            elif zero == True:
                allz = True
            else:
                zero = True
                
        ret = nums
        for i in range(len(nums)):
            if nums[i] != 0:
                ret[i] = total // nums[i]
                if zero == True:
                    ret[i] = 0
                
            elif allz == True:
                ret[i] = 0
            else:
                ret[i] = total
        return ret