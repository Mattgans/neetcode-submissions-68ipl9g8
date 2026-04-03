import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_hours = 1000000001
        left = 1
        right = max(piles)
        print(right)
        while(left <= right):
            mid = (left+right)//2
            total = 0
            print(mid)
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid) 
            if (total <= h):
                min_hours = min(min_hours, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_hours
    