
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""

迭代法：

时间复杂度：O(n)，其中 n 是链表的长度

空间复杂度：O(1)，只需要常数级别的额外空间

使用哑节点简化链表头部的交换操作

递归法：

时间复杂度：O(n)

空间复杂度：O(n)，递归调用栈的深度

代码更简洁但空间复杂度较高

"""
def swapPairs(head: ListNode) -> ListNode:
    # 创建哑节点作为链表头的前驱节点
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        # 要交换的两个节点
        first = head
        second = head.next

        # 执行交换
        prev.next = second
        first.next = second.next
        second.next = first

        # 移动指针到下一对的前驱位置
        prev = first
        head = first.next

    return dummy.next


def swapPairs2(head: ListNode) -> ListNode:
    # 递归终止条件：没有节点或只有一个节点
    if not head or not head.next:
        return head

    # 要交换的两个节点
    first = head
    second = head.next

    # 递归交换后面的节点
    first.next = swapPairs(second.next)
    second.next = first

    # 返回新的头节点
    return second