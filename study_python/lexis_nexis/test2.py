"""

因候选人提到对该类暂不熟悉，暂时无法解出，对字符串相对熟悉一些。题目更新为求取两个字符串的最长公共子序列做进一步探讨。具体题目如下：

给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。


提示：

1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。

"""

def length_of_max_substr(txt1, txt2):
    count =0
    max_substr = ""
    for i in txt1:
        # print(i)
        if i in txt2:
            count += 1


    return max_substr

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "aec"

    max_substr = length_of_max_substr(text1, text2)
    print(max_substr)

    text1 = "abc"
    text2 = "abc"

    max_substr = length_of_max_substr(text1, text2)
    print(max_substr)

    text1 = "abc"
    text2 = "def"

    max_substr = length_of_max_substr(text1, text2)
    print(max_substr)

