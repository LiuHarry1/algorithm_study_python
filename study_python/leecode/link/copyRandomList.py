
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

            # 第一次遍历：创建所有新节点并建立原节点到新节点的映射
        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # 第二次遍历：设置next和random指针
        current = head
        while current:
            if current.next:
                node_map[current].next = node_map[current.next]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next

        return node_map[head]