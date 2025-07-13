
class Solution():

    def kthSmallest(self, root, k):

        self.k = k
        self.result = None

        def inorder(root):

            if not root or self.result is not None:
                return

            inorder(root.left)

            self.k -=1
            if self.k==0:
                self.result = root.val
                return
            inorder(root.right)

        inorder(root)
        return self.result

    def kthSmallest_stack(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

