class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1 
        low = 0
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        low = l


        if target >= nums[0]:
            l = 0
            r = (low - 1 if low > 0 else len(nums) - 1)
        elif target <= nums[-1]:
            l = low
            r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid +  1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid

        return -1