

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self.right= right

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.inorderTraversal(root)
    print(result)


