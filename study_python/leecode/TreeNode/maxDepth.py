# 104. 二叉树的最大深度
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self.right = right

# 递归解法（DFS）
# 时间复杂度：O(n)，需要访问树中的所有节点
# 空间复杂度：O(h)，其中h是树的高度，递归调用栈的深度

def maxDepth_DFS(root):

    if not root:
        return 0

    left_depth = maxDepth_DFS(root.left)
    right_depth = maxDepth_DFS(root.right)

    return max(left_depth, right_depth) +1



"""
使用栈来实现深度优先搜索的迭代版本。
时间复杂度：O(n)
空间复杂度：O(h)，h是树的高度
"""
def stack_maxDepth_DFS(root):
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node , depth = stack.pop()
        max_depth = max(depth, max_depth)

        if node.left:
            stack.append((node.left, depth+1))
        if node.right:
            stack.append((node.right, depth +1))


    return max_depth

def queue_maxDepth(root):

    if not root:
        return 0

    # 正确初始化deque
    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth





def build_sample_tree():
    """构建一个示例二叉树"""
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

if __name__ == '__main__':
    # root = build_sample_tree()
    # result = stack_maxDepth_DFS(root)
    # result = maxDepth_DFS(root)
    # print(result)

    stack = [1,2]
    stack.append(3)
    print(stack)
    print(stack.pop())
