class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        cur = ""
        for l in s:
            if l not in cur:
                cur += l
            else:
                while l in cur:
                    cur = cur[1:]
                cur += l
            best = max(best,len(cur))
        return best