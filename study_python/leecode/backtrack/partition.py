class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        res = []
        backtrack(0, [])
        return res