

class listNode:

    def __init__(self, val):
        self.val = val
        self.next =None

def reverseList(head:listNode) -> listNode:

    pre = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = pre
        pre = curr
        curr = next_node

    return pre


if __name__ == '__main__':
    head = listNode(1)
    head.next = listNode(2)
    head.next.next = listNode(3)
    head.next.next.next = listNode(4)

    revsered_list = reverseList(head)

    while revsered_list:
        print(revsered_list.val)
        revsered_list = revsered_list.next