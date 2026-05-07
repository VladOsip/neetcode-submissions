class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                square_idx = (r // 3) * 3 + (c // 3)

                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_idx]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[square_idx].add(val)

        return True
