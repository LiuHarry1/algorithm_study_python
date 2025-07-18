
def longestValidParentheses(s):
    n = len(s)

    if n==0:
        return 0

    dp = [0] *n
    dp[0] =0
    max_len = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i-1]=='(':
                dp[i] =  2 + (dp[i-2] if i >=2 else 0)
            else:
                j = i - dp[i-1] -1
                if j>=0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[j-1] if j>=1 else 0)

            max_len = max(max_len, dp[i])

    return max_len