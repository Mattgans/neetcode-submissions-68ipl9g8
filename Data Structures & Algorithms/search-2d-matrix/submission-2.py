class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1
        while(top <= bot):
            mid = (top + bot)// 2
            if mid != len(matrix)-1 and matrix[mid][0] <= target and matrix[mid+1][0] > target:
                break
            if mid == len(matrix)-1 and matrix[mid][0] <= target:
                break
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1

        left = 0
        right = len(matrix[0]) - 1
        while(left <= right):
            center = (left + right) // 2
            if matrix[mid][center] == target:
                return True
            elif matrix[mid][center] < target:
                left = center + 1
            else:
                right = center - 1

        return False


        # while(target < matrix[row][0]):
        #     row += 1


        # left = 0
        # right = len(nums)-1
        # while(left <= right):
        #     mid = (left+right) // 2
        #     print(mid)

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid-1
        # return -1
