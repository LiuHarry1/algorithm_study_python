

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self.right= right

class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def preorder(node: TreeNode):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    print(sol.preorderTraversal(root))  # 输出：[1, 2, 3]


