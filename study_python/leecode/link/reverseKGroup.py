# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, tail):
            """翻转 head 到 tail 之间的链表（不包括 tail）"""
            prev = tail  # 翻转后的链表应该连接到 tail
            curr = head
            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  # 返回翻转后的头节点

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev 指向当前组的头节点的前一个节点

        while head:
            tail = prev
            # 检查剩余部分是否至少有 k 个节点
            for _ in range(k):
                tail = tail.next
                if not tail:  # 不足 k 个，直接返回
                    return dummy.next

            next_group = tail.next  # 记录下一组的起始节点
            # 翻转当前组
            new_head = reverse(head, tail.next)
            # 连接翻转后的链表
            prev.next = new_head
            # 更新 prev 和 head 到下一组的起始位置
            prev = head
            head = next_group

        return dummy.next