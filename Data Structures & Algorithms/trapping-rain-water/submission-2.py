class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers bitches
        l = 0
        r = len(height)-1
        left = height[l]
        right = height[r]
        max_size = 0
        while(l < r):
            if left < right:
                l += 1
                left = max(left, height[l])
                max_size += left - height[l]
            else:
                r -= 1
                right = max(right,height[r])
                max_size += right - height[r]
        return max_size

        

        

                
        