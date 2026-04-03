class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        ret = []
        for i in range(k):
            ret.append(max(counts, key = counts.get))
            counts.pop(max(counts, key = counts.get))
        return ret