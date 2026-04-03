class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best_area = 0
        while left < right:
            if min(heights[left],heights[right]) * (right-left) > best_area:
                best_area = min(heights[left],heights[right]) * (right-left)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
            
        return best_area

            
        