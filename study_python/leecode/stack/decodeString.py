def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


# 测试用例
if __name__ == "__main__":
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        # ("3[a2[c]]", "accaccacc"),
        # ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        # ("abc3[cd]xyz", "abccdcdcdxyz"),
        # ("10[a]", "aaaaaaaaaa")
    ]

    for s, expected in test_cases:
        result = decodeString(s)
        print(f"输入: {s}")
        print(f"预期: {expected}")
        print(f"结果: {result}")
        print("通过" if result == expected else "失败")
        print()