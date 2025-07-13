"""

114. 二叉树展开为链表
"""

def flatten(root):

    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    left =root.left
    right = root.right

    root.left = None
    root.right = left


    p = root
    while p.right:
        p = p.right

    p.right = right
