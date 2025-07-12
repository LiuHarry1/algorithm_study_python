# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next


def get_sub_list(cur, step):
    left = cur
    for _ in range(step - 1):
        if not cur.next:
            break
        cur = cur.next
    right = cur.next
    cur.next = None  # 切断子链表
    return left, right


def sortList(head):
    if not head or not head.next:
        return head

    # 计算链表长度
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    dummy = ListNode(-1)
    dummy.next = head

    step = 1
    while step < length:
        prev, curr = dummy, dummy.next

        while curr:
            # 获取第一个子链表
            left, curr = get_sub_list(curr, step)

            # 如果没有剩余节点，直接连接第一个子链表
            if not curr:
                prev.next = left
                break

            # 获取第二个子链表
            right, curr = get_sub_list(curr, step)

            # 合并两个子链表
            merged = merge(left, right)
            prev.next = merged

            # 移动prev到合并后链表的末尾
            while prev.next:
                prev = prev.next

        step *= 2

    return dummy.next
