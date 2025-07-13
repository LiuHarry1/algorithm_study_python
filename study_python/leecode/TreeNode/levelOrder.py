from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):

    if not root:
        return []

    result = []

    dq= deque([root])

    while dq:
        length = len(dq)
        current_level = []

        for i in range(length):
            node = dq.popleft()
            current_level.append(node.val)

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        result.append(current_level)

    return result