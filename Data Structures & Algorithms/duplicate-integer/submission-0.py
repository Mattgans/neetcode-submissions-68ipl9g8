class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = []
        for x in nums:
            if x in counts:
                return True
            else:
                counts.append(x)
        return False