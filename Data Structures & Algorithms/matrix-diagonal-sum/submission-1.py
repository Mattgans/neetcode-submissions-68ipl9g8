class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            # print(mat[i][i])
            total += mat[i][(-i) -1]
        if len(mat) % 2 != 0:
            total -= mat[len(mat)//2][len(mat)//2]
        return total