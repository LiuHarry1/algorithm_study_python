
"""
98. 验证二叉搜索树
中序遍历是一个递增数组。

"""
class Solution():
    def isValidBST(self, root):

        self.prev = -float('inf')

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False

            if self.prev >= root.val:
                return False
            self.prev = root.val

            return inorder(root.right)

        return inorder(root)