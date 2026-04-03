class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_num = sorted(set(nums))
        longest = 1
        current = 1

        for i in range(1, len(sorted_num)):
            if sorted_num[i] == sorted_num[i - 1] + 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1

        return longest        
        