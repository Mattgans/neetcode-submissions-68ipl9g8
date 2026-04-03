class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                squares[(r//3,c//3)].add(val)
        return True
        # for row in board:
        #     row_vals = []
        #     for col in row:
        #         if col in row_vals and col != ".":
        #             return False
        #         else:
        #             row_vals += col
        # for i in range(9):
        #     col_vals = []
        #     for j in range(9):
        #         if board[j][i] in col_vals and board[j][i] != ".":
        #             return False
        #         else:
        #             col_vals += board[j][i]
        # for i in range(3):
        #     for j in range(3):
        #         vals = []
        #         for k in range(3):
        #             for l in range(3):
        #                 val = board[3*i + k][3*j+l]
        #                 if val in vals and val != ".":
        #                     return False
        #                 else:
        #                     vals += val
        # return True
                
        