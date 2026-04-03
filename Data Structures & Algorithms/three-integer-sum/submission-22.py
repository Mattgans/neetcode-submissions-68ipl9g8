class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer
        nums = sorted(nums)
        ret =[]
        for mid in range(1,len(nums)-1):
            left = 0
            right = len(nums)-1
            target = -nums[mid]
            while(left < mid and right > mid):
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] == target:
                    add = [nums[left], nums[mid], nums[right]]
                    if add not in ret:
                        ret.append(add)
                    left += 1
                    right -= 1
        return ret
                


        # # brute force
        # ret = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 r = sorted([nums[i], nums[j], nums[k]])
        #                 if r not in ret:
        #                     ret.append(r)
                            
        # return ret

        