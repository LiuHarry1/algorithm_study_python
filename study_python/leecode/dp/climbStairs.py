

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def climbStairs_new(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second