class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1
        while top <= bot:
            mid = (top + bot)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        if(top > bot):
            return False
        best_row = (top+bot)//2
        left = 0
        right = len(matrix[best_row])-1
        while left <= right:
            mid = (left + right) //2
            if target > matrix[best_row][mid]:
                left = mid + 1
            elif target < matrix[best_row][mid]:
                right = mid - 1
            else:
                return True
        
        return False


