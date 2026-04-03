class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nset = {}

        for r in range(len(nums)):
            diff = target - nums[r]
            if nset.get(diff,-1) != -1:
                return [nset.get(diff),r]
            nset[nums[r]] = r
            
            