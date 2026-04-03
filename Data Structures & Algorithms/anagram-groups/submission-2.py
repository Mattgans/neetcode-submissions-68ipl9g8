class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            cur = {}
            for char in s:
                cur[char] = cur.get(char, 0) + 1
            counts[tuple(sorted(cur.items()))].append(s)
        
        return list(counts.values())
