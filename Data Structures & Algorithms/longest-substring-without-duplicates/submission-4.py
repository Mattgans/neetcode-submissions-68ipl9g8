class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char = set()
        max_l = 0
        while(right < len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            max_l = max(max_l,right-left+1)
            right+=1
        return max_l

            
