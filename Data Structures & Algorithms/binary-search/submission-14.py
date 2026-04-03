class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
            if right-left == 1:
                return -1
        return -1                
