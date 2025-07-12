# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        # 分治法合并
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next

        # 两两合并，直到只剩一个链表
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")

if __name__ == '__main__':
    # 测试示例 1
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    sol = Solution()
    result = sol.mergeKLists(lists)
    print_list(result)  # 输出: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

    # 测试示例 2
    lists = []
    result = sol.mergeKLists(lists)
    print_list(result)  # 输出: None

    # 测试示例 3
    lists = [None]
    result = sol.mergeKLists(lists)
    print_list(result)  # 输出: None