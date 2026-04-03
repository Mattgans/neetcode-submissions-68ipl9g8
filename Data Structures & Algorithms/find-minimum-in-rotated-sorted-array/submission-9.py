class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            mid = (left+(right))//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            print(nums[left])
        return nums[left]
                

        
        
        
        # # even faster 
        # return min(nums)

        # # brute force
        # ret = float("inf")
        # for num in nums:
        #     ret = min(ret, num)
        # return ret
        