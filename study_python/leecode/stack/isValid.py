"""

20. 有效的括号
"""

class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # 当前字符是右括号
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:  # 当前字符是左括号
                stack.append(char)

        return not stack