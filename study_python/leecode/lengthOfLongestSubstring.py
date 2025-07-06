
"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution(object):

    def getSubstr(self, str, char):
        pass
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0

        left =0
        char_set = set()


        for right in range(0, len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1

            char_set.add(s[right])

            max_len = max(max_len, (right -left +1))

        return max_len


if __name__ == '__main__':
    solution = Solution();

    longest_substr = solution.lengthOfLongestSubstring("abcabcbb")
    print(longest_substr)
    longest_substr = solution.lengthOfLongestSubstring("bbbbb")
    print(longest_substr)
    longest_substr = solution.lengthOfLongestSubstring("pwwkew")
    print(longest_substr)