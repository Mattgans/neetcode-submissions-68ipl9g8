class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        for num in counts.values():
            print(num)
            if num > 1:
                return True
        return False