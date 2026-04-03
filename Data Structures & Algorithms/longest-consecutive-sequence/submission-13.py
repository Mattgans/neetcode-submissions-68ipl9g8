class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force first
        tot = 0
        for i in range(len(nums)):
            count = 1
            val = nums[i]
            while(True):
                if val + 1 in nums:
                    val += 1
                    count += 1
                else:
                    break
            tot = max(tot,count)

        return tot
                  
                

                    
        