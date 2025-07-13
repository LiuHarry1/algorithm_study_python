from collections import deque

from collections import deque
from typing import List, Optional

"""
199. 二叉树的右视图
层序遍历， 取每一层的最后一个数。

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # 记录每一层的最后一个节点
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def rightSideView_new(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            # 如果当前深度等于结果列表长度，说明这是该层第一个被访问的节点（从右看）
            if depth == len(result):
                result.append(node.val)
            # 先访问右子树，再访问左子树
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result