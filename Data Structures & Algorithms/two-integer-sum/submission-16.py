class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(0,i):
        #         if nums[i] + nums[j] == target:
        #             return [j,i]
        # return [0,0]

        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff],i]
            prev[n] = i