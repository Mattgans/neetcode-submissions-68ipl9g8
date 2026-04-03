class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:
            mid = (l+r) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p) / mid)
            if total <= h:
                best = min(best,mid)
                r = mid - 1
            else:
                l = mid + 1
        return best
