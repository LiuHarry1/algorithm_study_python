
"""

143. 重排链表

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):

    prev = None
    cur =head

    while cur:
        tmp = cur.next
        cur.next =prev
        prev = cur
        cur = tmp

    return prev



class Solution:
    def reorderList(self, head):

        if not head and not head.next:
            return

        slow = fast = head

        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next


        reversed_slow = reverse(slow)

        first, second = head, reversed_slow

        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



