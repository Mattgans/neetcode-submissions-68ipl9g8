class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        total = n
        seen.add(total)
        count = 0
        while(True):
            new = 0
            print(seen)
            print(total)
            for i in list(str(total)):
                new += int(i) * int(i)
            if new == 1:
                return True
            elif new in seen:
                return False
            else:
                seen.add(new)
                total = new


        
        