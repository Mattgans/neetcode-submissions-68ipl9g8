class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for idx, val in enumerate(nums):
            check[val] = (idx+1)
        for idx, val in enumerate(nums):
            other = check.get((target - val),0) 
            if other != 0 and (other-1) != idx:
                return [idx,check[target-val] - 1]
