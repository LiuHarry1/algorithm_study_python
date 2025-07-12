"""
141. 环形链表

"""

class linkNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    if not head or head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

