class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = min(heights[left],heights[right]) * (right-left)
        while (left < right):
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
            cur = min(heights[left],heights[right]) * (right-left)
            best = max(best, cur)


        return best