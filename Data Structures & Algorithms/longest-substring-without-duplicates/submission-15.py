class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # best = 0
        # cur = ""
        # for l in s:
        #     if l not in cur:
        #         cur += l
        #     else:
        #         while l in cur:
        #             cur = cur[1:]
        #         cur += l
        #     best = max(best,len(cur))
        # return best
        best = 0
        n = len(s)
        for i in range(n):
            sub = s[i]
            for j in range(i+1,n):
                if s[j] not in sub:
                    sub += s[j]
                    
                else:
                    print(sub)
                    best = max(len(sub),best)
                    break
            best = max(len(sub),best)
        return best