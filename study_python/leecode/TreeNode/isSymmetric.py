from collections import deque


def is_mirror(left, right):

    if not left and not right:
        return True
    if not left or not  right:
        return False
    if left.val != right.val:
        return False

    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


def isSymmetric(root):

    if not root:
        return True

    return is_mirror(root.left, root.right)


def isSymetrix_deque(root):

    if not root:
        return True

    queue = deque()
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True



