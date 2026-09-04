class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        right = len(heights) -1
        ret = [right]
        tallest = heights[right]
        while right != 0:
            right -= 1
            if heights[right] > tallest:
                tallest = heights[right]
                ret += [right]
        return sorted(ret)
