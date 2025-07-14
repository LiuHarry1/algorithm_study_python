# 337. 打家劫舍 III


def rob(root):


    def rob_helper(node):

        if not node:
            return (0, 0)

        left = rob_helper(node.left)
        right = rob_helper(node.right)

        max_rob = node.val + left[1] + right[1]
        max_not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return max_rob, max_not_rob



    max_rob, max_not_rob = rob_helper(root)

    return max(max_rob, max_not_rob)