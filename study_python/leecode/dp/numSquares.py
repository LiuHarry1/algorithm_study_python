class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] *(n+1)
        dp[0] =0
        for i in range(1, n+1):
            min_val = i
            j=1
            while j*j <=i:
                min_val = min(min_val, dp[i-j*j] +1)
                j +=1

            dp[i] = min_val

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))  # 输出: 3 (4 + 4 + 4)
    print(sol.numSquares(13))  # 输出: 2 (4 + 9)
    print(sol.numSquares(1))  # 输出: 1 (1)
    print(sol.numSquares(4))  # 输出: 1 (4)
    print(sol.numSquares(0))  # 输出: 0 (特殊情况)