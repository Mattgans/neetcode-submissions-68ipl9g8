class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid = []
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    if ([nums[i],nums[left],nums[right]] not in valid):
                        valid.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1


        return valid
        