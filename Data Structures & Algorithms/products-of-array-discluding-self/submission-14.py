class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        for val in nums:
            if val == 0:
                zeros += 1
            else:
                total *= val
        if zeros > 1:
            total = 0
        ret = []
        for val in nums:
            if val != 0:
                if zeros == 1:
                    ret.append(0)
                else:
                    ret.append(total // val)
            else:
                ret.append(total)
        return ret
        