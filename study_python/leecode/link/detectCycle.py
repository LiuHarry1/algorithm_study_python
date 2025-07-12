class ListNode(object):

    def __init__(self, val, next):
        self.val =val
        self.next = next

def has_cycle(node):

    if not node or not node.next:
        return False, node

    slow =node
    fast = node

    while (slow !=fast):

        if not fast or not fast.next:
            return False, None


        slow = slow.next
        fast = fast.next.next

    return True, slow




def detectCycle(head):
    if not head or not head.next:
        return None

    slow = head  # 慢指针从head开始
    fast = head  # 快指针也从head开始

    has_cycle = False  # 初始设为False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # 找环的入口
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def detectCycle_hash(head: ListNode) -> ListNode:
    visited = set()
    current = head

    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next

    return None