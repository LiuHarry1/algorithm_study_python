# 198. 打家劫舍

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # dp[i] 表示偷窃到第i个房屋时能获得的最大金额
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # 选择偷当前房屋（加上i-2的金额）或者不偷（保持i-1的金额）
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


"""
空间优化版本
由于每次只需要前两个状态，我们可以用两个变量代替整个dp数组，将空间复杂度从O(n)降到O(1):
"""
def rob_new(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev_max = 0  # 相当于dp[i-2]
    curr_max = 0  # 相当于dp[i-1]

    for num in nums:
        # 计算当前最大值：偷当前房屋或者不偷
        temp = curr_max
        curr_max = max(prev_max + num, curr_max)
        prev_max = temp

    return curr_max