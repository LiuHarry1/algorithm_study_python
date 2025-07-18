class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 != 0:  # 总和是奇数，直接不可能
            return False

        target = total // 2
        dp = [False] * (target + 1)  # dp[i]表示能否凑出和i
        dp[0] = True  # 初始状态：不选任何数时和为0

        for num in nums:
            for i in range(target, num - 1, -1):  # 从后往前避免重复计算
                if dp[i - num]:  # 如果能凑出i-num，加上当前num就能凑出i
                    dp[i] = True

        return dp[target]  # 最后检查能否凑出target