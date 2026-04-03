class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer
        nums = sorted(nums)
        ret =[]
        print(nums)
        for mid in range(len(nums)):
            if mid > 0 and -nums[mid] == -nums[mid-1]:
                continue
            left = mid + 1
            right = len(nums)-1
            while(left < right):
                total = nums[mid] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                elif total == 0:
                    add = [nums[mid],nums[left],nums[right]]
                    ret.append(add)
                    left += 1
                    right -= 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1



            # while(left != mid and right != mid and left < right):
            #     if nums[left] + nums[right] > target:
            #         right -= 1
            #     elif nums[left] + nums[right] < target:
            #         left += 1
            #     elif nums[left] + nums[right] == target:
            #         add = [nums[left],nums[mid],nums[right]]
            #         if add not in ret:
            #             ret.append(add)
            #             left += 1
            #             right -= 1

                        
                    
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

        