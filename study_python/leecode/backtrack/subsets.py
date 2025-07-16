
"""
78. 子集
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""
def subsets(nums):
    res = []

    def backtrack(start, path):
        # res.append(path.copy())  # 添加当前路径到结果
        res.append(path[:])
        if len(path) == 3:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])  # 选择当前数字
            backtrack(i, path)  # 递归下一层
            path.pop()  # 撤销选择（回溯）

    backtrack(0, [])
    return res

if __name__ == '__main__':
    result = subsets([1,2,3])
    print(result)