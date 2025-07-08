"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例
1：

输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例
2：


输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例
3：

输入：root = [1, 2], p = 1, q = 2
输出：1

提示：

树中节点数目在范围[2, 105]
内。
-109 <= Node.val <= 109
所有
Node.val
互不相同 。
p != q
p
和
q
均存在于给定的二叉树中。

https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.right
    print(lowestCommonAncestor(root, p, q).val)  # 输出: 3

    p = root.left
    q = root.left.right.right
    print(lowestCommonAncestor(root, p, q).val)  # 输出: 5

    root = TreeNode(1)
    root.left = TreeNode(2)
    p = root
    q = root.left
    print(lowestCommonAncestor(root, p, q).val)  # 输出: 1