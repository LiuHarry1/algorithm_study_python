



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self.right= right

"""
pre = 根，左(left_size)， 右
inorder = 左((left_size))， 根， 右

"""

def buildTree(preorder, inorder):

    inorder_map= {val: idx for idx, val  in enumerate(inorder) }

    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start> pre_end:
            return None

        root_val = preorder[pre_start]
        root_idx = inorder_map.get(root_val)
        root= TreeNode(root_val)
        left_size=  root_idx - in_start

        root.left = helper(pre_start+1, pre_start+left_size, in_start, root_idx -1)
        root.right = helper(pre_start+left_size+1, pre_end, root_idx+1, in_end)

        return root

    return help(0, len(preorder)-1, 0 , len(inorder)-1)
