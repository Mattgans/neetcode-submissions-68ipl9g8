class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        freq = [[] for i in range(len(nums)+1)]
        for key, val in counts.items():
            freq[val].append(key)
        
        ret = []
        for i in range(len(nums),0,-1):
            for val in freq[i]:
                ret.append(val)
                if len(ret) == k:
                    return ret
        return ret
            
        