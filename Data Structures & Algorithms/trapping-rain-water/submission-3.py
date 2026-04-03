class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax, rmax = height[l], height[r]
        ret = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax,height[l])
                ret += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                ret += rmax - height[r]
        return ret

            