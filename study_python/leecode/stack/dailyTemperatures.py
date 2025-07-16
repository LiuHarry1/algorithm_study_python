def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # 单调栈，存储温度数组的索引

    for i in range(n):
        # 当栈不为空且当前温度大于栈顶温度时
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)

    return result


# 测试用例
if __name__ == "__main__":
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([55, 54, 53, 52], [0, 0, 0, 0]),
    ]

    for temps, expected in test_cases:
        result = dailyTemperatures(temps)
        print(f"输入: {temps}")
        print(f"预期: {expected}")
        print(f"结果: {result}")
        print("通过" if result == expected else "失败")
        print()