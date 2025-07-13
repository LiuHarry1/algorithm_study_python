class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 使用普通字典代替defaultdict
        prefix_sum_count = {}
        prefix_sum_count[0] = 1  # 初始化前缀和为0出现1次
        self.result = 0

        def dfs(node, current_sum):
            if not node:
                return

            # 计算当前路径和
            current_sum += node.val

            # 检查是否存在满足条件的前缀和
            needed = current_sum - targetSum
            self.result += prefix_sum_count.get(needed, 0)

            # 更新当前前缀和的计数
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            # 递归处理左右子树
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # 回溯，恢复状态
            prefix_sum_count[current_sum] -= 1
            if prefix_sum_count[current_sum] == 0:
                del prefix_sum_count[current_sum]

        dfs(root, 0)
        return self.result