class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search One pass
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1 








        # # Optimized Approach first with binary on finding the cut then binary searching the subsection that might contain the target
        # left = 0
        # right = len(nums)-1
        # switch = 0
        # while(left < right):
        #     mid = (left+right)//2
        #     if nums[mid] < nums[right]:
        #         right = mid
        #     else:
        #         left = mid + 1
        # # right side
        # if target <= nums[-1] and target >= nums[left]:
        #     print("hi")
        #     l = left
        #     r = len(nums)-1
        #     while(l <= r):
        #         m = (l+r)//2
        #         if target == nums[m]:
        #             return m
        #         elif target > nums[m]:
        #             l = m + 1
        #         else:
        #             r = m -1
        # else:
        #     l = 0
        #     r = left-1
        #     while(l <= r):
        #         m = (l+r)//2
        #         if target == nums[m]:
        #             return m
        #         elif target > nums[m]:
        #             l = m + 1
        #         else:
        #             r = m -1
        # return -1





        # # naive approach
        # try:
        #     return nums.index(target)
        # except:
        #     return -1