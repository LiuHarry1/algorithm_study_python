def findAnagrams(s, p):

    s_len = len(s)
    p_len = len(p)

    if s_len < p_len:
        return []

    p_count= [0] * 26
    s_count = [0] * 26

    for i in range(p_len):
        p_count[ord(p[i]) - ord('a')] +=1

    result = []

    for i in range(s_len):
        s_count[ord(s[i]) - ord('a')] += 1
        if i >= p_len:
            s_count[ord(s[i- p_len]) - ord('a')] -= 1

        if s_count == p_count:
            result.append(i-p_len +1)

    return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))  # 输出: [0, 6]