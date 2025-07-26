def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                print('i=',i, 'j=', j, "dp[i]", dp[i])
                break
    return dp[n]


if __name__ == '__main__':
    s = "leetcode"
    word_dict = ['leet', 'code']
    result = wordBreak(s, word_dict)
    print(result)