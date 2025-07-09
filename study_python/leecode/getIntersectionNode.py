class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA

# 辅助函数：根据数组构建链表，并返回头节点
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# 构造公共部分
common = build_list([8, 4, 5])

# 构造 listA 的前半部分并连接到公共部分
headA = build_list([4, 1])
tailA = headA
while tailA.next:
    tailA = tailA.next
tailA.next = common  # 相交于 8

# 构造 listB 的前半部分并连接到公共部分
headB = build_list([5, 6, 1])
tailB = headB
while tailB.next:
    tailB = tailB.next
tailB.next = common  # 相交于 8

# 调用函数并打印结果
intersection = getIntersectionNode(headA, headB)
if intersection:
    print(f"Intersected at '{intersection.val}'")
else:
    print("No intersection")
