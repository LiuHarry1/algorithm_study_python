class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # 如果全部匹配，返回 True
            if index == len(word):
                return True
            # 检查越界或不匹配的情况
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            # 临时标记已访问
            temp, board[r][c] = board[r][c], '#'
            # 递归搜索四个方向
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            # 恢复状态
            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    sol = Solution()
    print(sol.exist(board, "ABCCED"))  # True
    print(sol.exist(board, "SEE"))  # True
    print(sol.exist(board, "ABCB"))  # False