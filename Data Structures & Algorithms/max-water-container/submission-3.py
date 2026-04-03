class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_size = 0
        while(l < r):
            height = min(heights[l],heights[r])
            width = r-l
            max_size = max(max_size, height*width)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_size


        