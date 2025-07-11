class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: ListNode):

    pre = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre


def isPalindrome( head: ListNode):
    if not head or not head.next:
        return True
    #找中点

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast =  fast.next.next

    second = reverse(slow)
    first = head

    while second:
        if first.val != second.val:
            return False

        first = first.next
        second = second.next

    return True



if __name__ == '__main__':
    # 示例1: 1->2->2->1
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    print(isPalindrome(node1))  # 输出: True

    # 示例2: 1->2
    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    print(isPalindrome(node1))  # 输出: False