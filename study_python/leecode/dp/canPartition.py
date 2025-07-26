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

    def canPartition_two_dimission(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)

        # 初始化dp数组，dp[i][j]表示前i个数字中能否选出一些数使得和为j
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # 初始条件：和为0时总是可以达到（不选任何数）
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j < nums[i - 1]:
                    # 当前数字太大，不能选
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可以选择不选当前数字，或者选当前数字
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]

    def canPartition_backtrack(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        nums.sort(reverse=True)  # 排序可以提前剪枝

        def backtrack(start, current_sum):
            if current_sum == target:
                return True
            if current_sum > target:
                return False
            for i in range(start, len(nums)):
                # 跳过重复元素（可选优化）
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if backtrack(i + 1, current_sum + nums[i]):
                    return True
            return False

        return backtrack(0, 0)


if __name__ == '__main__':
    solution = Solution()
    solution.canPartition()