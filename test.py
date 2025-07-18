class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [1] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(1, n + 1):
            dp[i] = max(dp[i], 1 + dp[i - 1])

        return dp[n]

        pre_max = 1
        cur_max = 0

        for i in range(n):
            tmp = cur_max
            cur_max = max(pre_max + 1, cur_max)
            pre_max = tmp

        return cur_max