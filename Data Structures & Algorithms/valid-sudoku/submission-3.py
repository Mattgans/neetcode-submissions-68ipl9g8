class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_vals = []
            for col in row:
                if col in row_vals and col != ".":
                    return False
                else:
                    row_vals += col
        for i in range(9):
            col_vals = []
            for j in range(9):
                if board[j][i] in col_vals and board[j][i] != ".":
                    return False
                else:
                    col_vals += board[j][i]
        for i in range(3):
            for j in range(3):
                vals = []
                for k in range(3):
                    for l in range(3):
                        val = board[3*i + k][3*j+l]
                        if val in vals and val != ".":
                            return False
                        else:
                            vals += val
        return True
                
        