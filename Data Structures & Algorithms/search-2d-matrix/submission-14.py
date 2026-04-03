class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row with first num that is less than target
        # then just binary from there
        l, r = 0, len(matrix)-1
        row = -1
        while l <= r:
            mid = (l+r)// 2
            if (mid == len(matrix)-1) or (matrix[mid][0] <= target and matrix[mid+1][0] > target):
                row = mid
                break
            elif (matrix[mid][0] > target):
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        
        