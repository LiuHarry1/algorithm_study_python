"""
46. 全排列

"""

def permute(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    res = []
    used = [False] * len(nums)
    backtrack([], used)
    return res