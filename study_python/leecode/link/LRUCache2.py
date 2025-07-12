class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def insert_after(self, node):
        """将当前节点插入到指定节点之后"""
        node.next.prev = self
        self.next = node.next
        node.next = self
        self.prev = node

    def remove(self):
        """从链表中移除当前节点"""
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            node.insert_after(self.head)  # 插入到头部
            self.size += 1
            if self.size > self.capacity:
                removed = self.tail.prev
                removed.remove()
                del self.cache[removed.key]
                self.size -= 1

    def _move_to_head(self, node):
        """将节点移动到头部"""
        node.remove()
        node.insert_after(self.head)