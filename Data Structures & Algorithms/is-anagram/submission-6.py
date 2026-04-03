class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}
        for char in s:
            set1[char] = set1.get(char, 0) + 1
        for char in t:
            set2[char] = set2.get(char,0) + 1
        if (len(s) != len(t)):
            return False
        for char in s:
            if set1.get(char,0) != set2.get(char,0):
                return False
        return True