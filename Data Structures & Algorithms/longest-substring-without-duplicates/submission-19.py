class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ret = 0

        for l in range(len(s)):
            while s[l] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[l])
            ret = max(ret,l - left + 1)
        return ret
