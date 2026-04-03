class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            cur = [0] * 26
            for c in s:
                cur[ord(c)-ord('a')] += 1
            counts[tuple(cur)].append(s)
        
        return list(counts.values())
