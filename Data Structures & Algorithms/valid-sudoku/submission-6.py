class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if row not in rows:
                    rows[row] = set()
                if col not in cols:
                    cols[col] = set()
                if (row//3,col//3) not in squares:
                    squares[(row//3,col//3)] = set()
                if (val in rows[row] or val in cols[col] or val in squares[(row//3,col//3)]):
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[row//3,col//3].add(val)
        return True
