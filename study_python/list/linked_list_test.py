
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None;

def insert_node(node, data):

    if node is None:
        return

    new_node = LinkedNode(data)
    cur = node
    while cur.next is not None:
        cur = cur.next

    cur.next = new_node


def print_node(node):

    cur = node

    while cur is not None:
        print(cur.val, "\t")
        cur = cur.next


if __name__ == '__main__':
    head = LinkedNode(1)
    head.next =LinkedNode(3)
    head.next.next = LinkedNode(5)
    head.next.next.next = LinkedNode(789)


    tmp= head

    tmp = tmp.next
    # tmp.next = None

    root = LinkedNode(1)

    insert_node(root, 3)
    insert_node(root, 4)
    insert_node(root, 5)
    insert_node(root, 5)

    print(root);
    print_node(root)

