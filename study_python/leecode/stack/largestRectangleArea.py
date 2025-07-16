def largestRectangleArea(heights):
    stack = []
    max_area = 0
    # 添加哨兵节点，处理边界情况
    heights = [0] + heights + [0]
    n = len(heights)

    for i in range(n):
        # 当当前高度小于栈顶高度时，计算栈顶高度的矩形面积
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            # 宽度 = 当前索引 - 新栈顶索引 - 1
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


# 测试用例
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),  # 最大矩形是高度5和6的两个柱子组成的10
    ]

    for heights, expected in test_cases:
        result = largestRectangleArea(heights)
        print(f"输入: {heights}")
        print(f"预期最大面积: {expected}")
        print(f"计算结果: {result}")
        print("通过" if result == expected else "失败")
        print()