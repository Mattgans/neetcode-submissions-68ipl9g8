class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for l in s:
            if counts.get(l,0) == 0:
                counts[l] = 1
            else:
                counts[l] += 1
        for j in t:
            if counts.get(j,0) == 0:
                return False
            else:
                counts[j] -= 1
        for val in counts.values():
            if val != 0:
                return False
        return True