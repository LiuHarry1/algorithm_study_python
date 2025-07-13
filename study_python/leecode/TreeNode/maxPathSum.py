# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')  # 初始化最大路径和为负无穷

        def max_gain(node):
            if not node:
                return 0

            # 递归计算左右子树的最大贡献值
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 当前节点作为路径转折点时的路径和
            price_newpath = node.val + left_gain + right_gain

            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, price_newpath)

            # 返回当前节点的最大贡献值（只能选择左右子树中的一个）
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum