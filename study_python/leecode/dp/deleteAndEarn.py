#740. 删除并获得点数


def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    max_num = max(nums)
    points = [0] * (max_num + 1)

    # 统计每个数字的总点数
    for num in nums:
        points[num] += num

    # 动态规划，类似打家劫舍问题
    prev_max = 0
    curr_max = 0

    for i in range(len(points)):
        temp = curr_max
        curr_max = max(prev_max + points[i], curr_max)
        prev_max = temp

    return curr_max