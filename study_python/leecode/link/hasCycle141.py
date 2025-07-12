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

    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False