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


# 辅助函数：将列表转换为链表
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# 辅助函数：将链表转换为列表（方便比较）
def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


if __name__ == "__main__":
    sol = Solution()

    # 测试用例：head = [1,2,3,4,5], k = 3
    input_list = [1, 2, 3, 4, 5]
    k = 3
    expected_output = [3, 2, 1, 4, 5]

    # 执行翻转
    head = list_to_linkedlist(input_list)
    result = sol.reverseKGroup(head, k)
    result_list = linkedlist_to_list(result)

    # 验证结果
    print(f"Input: {input_list}, k = {k}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {result_list}")
    print("Test Passed!" if result_list == expected_output else "Test Failed!")