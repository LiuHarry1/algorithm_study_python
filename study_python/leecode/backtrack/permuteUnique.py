"""
47. 全排列 II

"""

class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # 如果当前数字已被使用，或者与前一个数字相同且前一个数字未被使用
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        nums.sort()
        res = []
        used = [False] * len(nums)
        backtrack([], used)
        return res