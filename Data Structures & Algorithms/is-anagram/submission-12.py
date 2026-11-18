class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for l in s:
            counts[l] = counts.get(l,0) + 1
        for l in t:
            counts[l] = counts.get(l,0) - 1
        for v in counts.values():
            if v != 0:
                return False

        return True