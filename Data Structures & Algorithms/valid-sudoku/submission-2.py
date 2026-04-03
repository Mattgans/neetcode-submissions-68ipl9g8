class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False

        for outer_row in range(3):
            for outer_col in range(3):
                seen = set()
                for inner_row in range(outer_row * 3,outer_row * 3+3 ):
                    for inner_col in range(outer_col * 3,outer_col * 3+3):
                        if board[inner_row][inner_col] not in seen  or board[inner_row][inner_col] == ".":
                            seen.add(board[inner_row][inner_col])
                        else:
                            return False
        return True
                        
        