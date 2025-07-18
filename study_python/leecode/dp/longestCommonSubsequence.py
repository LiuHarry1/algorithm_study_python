

def longestCommonSubsequence(text1, text2):

    m ,n = len(text1), len(text2)

    dp = [[0]*(n+1)  for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    print(dp)
    return dp[m][n]



if __name__ == '__main__':
    text1 = "abcde"
    # text2 = "ace"
    text2 = "aec"

    max_substr = longestCommonSubsequence(text1, text2)
    print(max_substr)

    text1 = "abc"
    text2 = "abc"

    max_substr = longestCommonSubsequence(text1, text2)
    print(max_substr)

    text1 = "abc"
    text2 = "def"

    max_substr = longestCommonSubsequence(text1, text2)
    print(max_substr)
