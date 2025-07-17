class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 先检查是否本身就是完全平方数
        if int(n ** 0.5) ** 2 == n:
            return 1

        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 基础情况

        max_square = int(n ** 0.5) + 1
        square_nums = [i * i for i in range(1, max_square)]

        for i in range(1, n + 1):
            for square in square_nums:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))  # 输出: 3 (4 + 4 + 4)
    print(sol.numSquares(13))  # 输出: 2 (4 + 9)
    print(sol.numSquares(1))  # 输出: 1 (1)
    print(sol.numSquares(4))  # 输出: 1 (4)
    print(sol.numSquares(0))  # 输出: 0 (特殊情况)