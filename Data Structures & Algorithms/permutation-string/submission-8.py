class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = [0] * 26
        if (len(s1) > len(s2)):
            return False
        for s in s1:
            counts[ord(s)-97] += 1
        l = len(s1)
        counts2 = [0] * 26
        for i in range(len(s1)):
            counts2[ord(s2[i])-97] += 1
        if counts == counts2:
            return True
        while(l < len(s2)):
            counts2[ord(s2[l]) -97] += 1
            counts2[ord(s2[l-len(s1)])-97] -= 1
            l += 1
            if counts == counts2:
                return True
        return False
            