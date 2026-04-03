class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ret = []
        # nums = sorted(nums)
        # for m in range(1,len(nums)-1):
        #     target = -nums[m]
        #     l = 0
        #     r = len(nums) - 1
        #     while l < m and m < r:
        #         if nums[l] + nums[r] < target:
        #             l += 1
        #             continue
        #         if nums[l] + nums[r] > target:
        #             r -= 1
        #             continue
        #         if nums[l] + nums[r] == target:
        #             if [nums[l],nums[m],nums[r]] not in ret:

        #                 ret.append([nums[l],nums[m],nums[r]])
        #             l += 1
        #             r -= 1
        # return ret
        ret = []
        nums = sorted(nums)
        for target in range(0,len(nums)-2):
            if target > 0 and nums[target] == nums[target-1]:
                continue
            l = target + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[target] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[target] > 0:
                    r -= 1
                else:
                    ret.append([nums[l],nums[r],nums[target]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret
