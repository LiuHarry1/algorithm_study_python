# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            # 创建根节点
            root = TreeNode(nums[mid])

            # 递归构建左子树和右子树
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)


def printTree(root: TreeNode, level=0, prefix="Root: "):
    """辅助函数：打印二叉树"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            printTree(root.left, level + 1, "L--- ")
            printTree(root.right, level + 1, "R--- ")


def main():
    solution = Solution()

    # 测试用例1
    nums1 = [-10, -3, 0, 5, 9]
    print("输入数组:", nums1)
    tree1 = solution.sortedArrayToBST(nums1)
    print("生成的BST:")
    printTree(tree1)

    # 测试用例2
    nums2 = [1, 3]
    print("\n输入数组:", nums2)
    tree2 = solution.sortedArrayToBST(nums2)
    print("生成的BST:")
    printTree(tree2)


if __name__ == "__main__":
    main()