
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """

    dummy = ListNode(-1)
    dummy.next= head

    slow = fast = dummy

    for _ in range(n+1):
        fast= fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next= slow.next.next

    return dummy.next