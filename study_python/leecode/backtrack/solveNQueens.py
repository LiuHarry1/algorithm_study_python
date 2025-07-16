class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                # 检查当前列、主对角线、副对角线是否冲突
                if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    board[row][col] = 'Q'  # 放置皇后
                    # 记录已占用的列和对角线
                    backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
                    board[row][col] = '.'  # 回溯

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set())
        return res