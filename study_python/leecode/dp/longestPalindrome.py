class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        self.start = 0
        self.max_len = 1

        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # 当前回文长度为 right - left - 1
            if right - left - 1 > self.max_len:
                self.start = left + 1
                self.max_len = right - left - 1

        for i in range(n):
            expand_around_center(i, i)  # 奇数长度
            expand_around_center(i, i + 1)  # 偶数长度

        return s[self.start:self.start + self.max_len]