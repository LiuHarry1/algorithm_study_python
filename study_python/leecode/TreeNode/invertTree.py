class TreeNode():

    def __init__(self, val):
        self.val =val
        self.right = None
        self.left = None


"""
时间复杂度：O(n)，每个节点都会被访问一次

空间复杂度：O(h)，递归栈的深度，h是树的高度
"""

def invert_tree(root: TreeNode):

    if not root:
        return None

    root.right , root.left = root.left, root.right
    invert_tree(root.left)
    invert_tree(root.right)

    return root




