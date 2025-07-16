def generateParenthesis(n):
    def backtrack(open_remain, close_remain, path):
        # 当所有括号都用完时，将当前组合加入结果
        if open_remain == 0 and close_remain == 0:
            res.append(''.join(path))
            return

        # 如果还有左括号可用，添加左括号
        if open_remain > 0:
            path.append('(')
            backtrack(open_remain - 1, close_remain, path)
            path.pop()  # 回溯

        # 只有在已添加的左括号比右括号多时，才能添加右括号
        if close_remain > open_remain:
            path.append(')')
            backtrack(open_remain, close_remain - 1, path)
            path.pop()  # 回溯

    res = []
    backtrack(n, n, [])
    return res


print(generateParenthesis(3))