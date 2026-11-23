class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = ""
        cur = ""
        for l in s:
            if l not in cur:
                cur += l
            else:
                if len(cur) > len(best):
                    best = cur     
                while l in cur:
                    cur = cur[1:]
                cur += l

        return max(len(best),len(cur))