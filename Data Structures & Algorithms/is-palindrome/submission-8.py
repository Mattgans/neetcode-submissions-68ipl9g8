class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        print(s)
        for i in range(len(s)//2):
            while((s[l].isalnum()) == False):
                l += 1
                if(l == r):
                    return True
            while((s[r].isalnum())== False):
                r -= 1
                if(l == r):
                    return True
            if(r == l):
                return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                print(l,r)
                return False
        return True