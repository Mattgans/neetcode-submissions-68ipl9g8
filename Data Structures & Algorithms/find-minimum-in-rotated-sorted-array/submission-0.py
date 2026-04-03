class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        ret = float("inf")
        for num in nums:
            ret = min(ret, num)
        return ret
        