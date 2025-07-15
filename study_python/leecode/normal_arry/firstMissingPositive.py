
"""

41. 缺失的第一个正数

"""



def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    # 1. 将所有<=0的数替换为n+1（这样它们就不会影响后面的步骤）
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    # 2. 对于每个存在的数字num，将nums[num-1]标记为负数
    for i in range(n):
        num = abs(nums[i])  # 取绝对值是因为可能有已经被标记为负数的元素
        if num <= n:  # 只处理1到n的数字
            nums[num - 1] = -abs(nums[num - 1])  # 确保即使已经是负数也保持不变

    # 3. 找到第一个正数的位置，其索引+1就是缺失的最小正数
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # 如果1到n都存在，则缺失的是n+1
    return n + 1



if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    result = firstMissingPositive(nums)
    print(result)