class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        for m in range(1,len(nums)-1):
            target = -nums[m]
            l = 0
            r = len(nums) - 1
            while l < m and m < r:
                if nums[l] + nums[r] < target:
                    l += 1
                    continue
                if nums[l] + nums[r] > target:
                    r -= 1
                    continue
                if nums[l] + nums[r] == target:
                    if [nums[l],nums[m],nums[r]] not in ret:

                        ret.append([nums[l],nums[m],nums[r]])
                    l += 1
                    r -= 1


        return ret
                
