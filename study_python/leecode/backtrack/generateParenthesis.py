class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def is_valid(s):
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:  # 出现多余的 ')'
                    return False
            return balance == 0  # 确保所有 '(' 都被匹配

        def backtrack(path, length):
            if length == 2 * n:
                # if is_valid(path):
                #     result.append("".join(path))
                print(path)
                return
            path.append('(')
            backtrack(path, length + 1)
            path.pop()
            path.append(')')
            backtrack(path, length + 1)
            path.pop()


        result = []
        backtrack([], 0)
        return result

if __name__ == '__main__':
    Solution().generateParenthesis(2)