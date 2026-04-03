class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        maxf = 0
        for char in range(len(s)):
            freq[s[char]] = freq.get(s[char], 0) + 1
            maxf = max(maxf, freq[s[char]])

            while(char - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, char-l+1)


        return res
