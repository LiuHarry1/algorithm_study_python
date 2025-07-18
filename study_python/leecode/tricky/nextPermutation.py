def nextPermutation(nums):
    """
    更简单易懂的下一个排列实现
    步骤：
    1. 从后向前找第一个下降的位置
    2. 从后向前找第一个比它大的数
    3. 交换这两个数
    4. 反转后面的部分
    """
    n = len(nums)

    # 1. 找第一个下降的位置（从后向前）
    pivot = n - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1

    # 如果不是完全降序排列（即不是最大排列）
    if pivot >= 0:
        # 2. 找第一个比nums[pivot]大的数（从后向前）
        swap_pos = n - 1
        while swap_pos > pivot and nums[swap_pos] <= nums[pivot]:
            swap_pos -= 1
        # 3. 交换这两个数
        nums[pivot], nums[swap_pos] = nums[swap_pos], nums[pivot]

    # 4. 反转pivot后面的部分（使其升序）
    nums[pivot + 1:] = nums[pivot + 1:][::-1]


# 测试用例
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],  # -> [1, 3, 2]
        [3, 2, 1],  # -> [1, 2, 3]
        [1, 1, 5],  # -> [1, 5, 1]
        [1, 3, 2],  # -> [2, 1, 3]
        [2, 3, 1]  # -> [3, 1, 2]
    ]

    for case in test_cases:
        original = case.copy()
        nextPermutation(case)
        print(f"输入: {original} -> 输出: {case}")