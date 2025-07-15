from collections import deque


class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # 初始化：统计新鲜橘子数量，并将腐烂橘子加入队列
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))  # (行, 列, 当前时间)

        if fresh == 0:  # 没有新鲜橘子直接返回0
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
        max_time = 0

        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # 标记为腐烂
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
                    max_time = max(max_time, time + 1)

        return max_time if fresh == 0 else -1