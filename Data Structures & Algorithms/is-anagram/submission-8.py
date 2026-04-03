class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = {}
        count_2 = {}
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            count_1[s[i]] = count_1.get(s[i],0) + 1
            count_2[t[i]] = count_2.get(t[i],0) + 1
        if count_1 == count_2:
            return True

        return False