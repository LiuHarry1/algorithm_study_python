class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.result = []

        def backtrack(path, open_remaining, close_remaining):
            if open_remaining==0:
                return

            if close_remaining == 0:
                self.result.append("".join(path))
                return

            # if open_remaining > 0:
            path.append("(")
            backtrack(path, open_remaining - 1, close_remaining)
            path.pop()

            # if close_remaining > open_remaining:
            path.append(")")
            backtrack(path, open_remaining, close_remaining - 1)
            path.pop()

        backtrack([], n, n)
        return self.result

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))  # 输出: ["((()))","(()())","(())()","()(())","()()()"]